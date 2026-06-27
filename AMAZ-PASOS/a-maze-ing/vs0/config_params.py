import re

class ConfigParams:
    width = -1
    height = -1
    start = [-1, -1]
    finish = [-1, -1] 
    out_file = "output_maze.txt"
    perfect = -1
    in_file = ""
    generate_maze = [[]] # deberia ser privado
    seed = None

    def __init__(self, filename):
        self.in_file = filename

    def parse(self):
        # Parse config file
        config_file = open(self.in_file, "r") # TODO add try-except. 
        #If file sys.argv[1] can not be found: print error and exit
        line_num = 1
        ret_val = False
        while line_num:
            # Read line and check validity
            line = config_file.readline()
            if line:
                if line[0] != '#': # Skip comments
                    if not self.parseLine(line):
                        print("ERROR: Could not parse line", line_num)
                        break
                line_num+=1
            else: # EOF
                line_num = 0
                if self.allParamsFilled(): # The following keys are mandatory
                    ret_val = True

        config_file.close()
        return ret_val

    def parseLine(self, line):
        line = line.rstrip('\r\n') # removes \r, \n and \r\n

        if line.startswith("WIDTH="):
            self.width = self.extractPositiveInt(line[6:])
            if self.width < 0:
                print("ERROR: failure parsing WIDTH's value")
                return False
        elif line.startswith("HEIGHT="):
            self.height = self.extractPositiveInt(line[7:])
            if self.height < 0:
                print("ERROR: failure parsing HEIGHT's value")
                return False
        elif line.startswith("ENTRY="):
            self.start[0], self.start[1] = self.extractPoint(line[6:])
            if self.start[0] < 0 or self.start[1] < 0 :
                print("ERROR: failure parsing ENTRY's values")
                return False
        elif line.startswith("EXIT="):
            self.finish[0], self.finish[1] = self.extractPoint(line[5:])
            if self.finish[0] < 0 or self.finish[1] < 0 :
                print("ERROR: failure parsing EXIT's values")
                return False
        elif line.startswith("OUTPUT_FILE="):
            self.out_file = self.extractFileName(line[12:])
            if not self.out_file:
                print("ERROR: failure parsing OUTPUT_FILE's name.")
                return False
        elif line.startswith("PERFECT="):
            self.perfect = self.extractBool(line[8:])
            if self.perfect < 0:
                print("ERROR: failure parsing PERFECT's value")
                return False
        elif line.startswith("SEED="):
            '''
            self.seed = self.extractPositiveInt(line[5:])
            if self.seed < 0:
                print("ERROR: failure parsing SEED's value")
                return False
            '''
            self.seed = self.extractPositiveInt(line[5:])
            if line[5:] != "None":
                if self.seed < 0:
                    print("ERROR: failure parsing SEED's value")
                    return False
            else:
                self.seed = None
            
        else:
            print("ERROR: unsupported tag. Check for spelling errors, spaces, tabs...")
            print("Supported tags are: WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT and SEED.")
            print("Correct format is \"TAG=value\"")
            return False
        return True

    def extractPositiveInt(self, str):
        val_str = re.findall("[0-9]+", str)
        if val_str and val_str[0]:
            if str == val_str[0]:
                return int(val_str[0])
        return -1

    def extractBool(self, str):
        if str.lower() == "true":
            return 1
        elif str.lower() == "false":
            return 0
        else:
            return -1
        
    def extractPoint(self, str):
        val_str = re.findall("[0-9]+", str)
        if len(val_str) == 2 and val_str[0] and val_str[1]:
            val = f"{val_str[0]},{val_str[1]}"
            if str == f"{val_str[0]},{val_str[1]}":
                return int(val_str[0]), int(val_str[1])
        return -1, -1

    def extractFileName(self, str):
        # String without spaces or within quotation marks
        if str:
            if (str.strip() == str or
                ((str[0] == '\'' or str[0] == '\"') and str[0] == str[:-1])):
                return str
        return ""

    def allParamsFilled(self): # estos son obligatorios - si no esta alguno de ellos da error
        return (self.width > 0 and self.height > 0 and
                self.start[0] >= 0 and self.start[1] >= 0 and
                self.finish[0] >= 0 and self.finish[1] >= 0 and
                self.out_file and self.perfect >= 0)
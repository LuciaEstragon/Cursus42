import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("\nNow show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth:")
try:
    print(f"{alchemy.create_earth()}")
except AttributeError as e:
    print(f"Traceback (most recent call last):\n...\nAttributeError: {e}")

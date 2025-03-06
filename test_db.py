import oracledb
import os

wallet_dir = os.path.abspath("oracle_wallet")

connection = oracledb.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dsn=os.getenv("DB_DSN"),
    wallet_password=os.getenv("WALLET_PASSWORD"),
    wallet_location=wallet_dir,
    config_dir=wallet_dir
)

cursor = connection.cursor()

# Sample test: Check database SYSDATE is returned successfully
cursor.execute("SELECT SYSDATE FROM dual")
result = cursor.fetchone()
assert result is not None, "Failed to fetch SYSDATE"
print(f"✅ Test passed! SYSDATE: {result[0]}")

# Add more database tests here
# Example:
cursor.execute("SELECT COUNT(*) FROM some_table")
count = cursor.fetchone()[0]
assert count >= 0, "some_table count should never be negative"

print("✅ All tests passed successfully!")

cursor.close()
connection.close()

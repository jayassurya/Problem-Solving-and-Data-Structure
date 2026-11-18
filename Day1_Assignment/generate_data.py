
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

BASE = Path(__file__).parent

def save_csv(folder, filename, headers, rows):
    path = BASE / folder / "data" / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created {path.relative_to(BASE)}: {len(rows)} records")


# --------------------------------------------------
# SET 1: RETAIL ORDER DESK
# --------------------------------------------------

def generate_orders():
    orders = []
    start = datetime(2026, 10, 1, 8, 0, 0)

    for i in range(50000):
        created = start + timedelta(
            seconds=random.randint(0, 7 * 24 * 60 * 60)
        )

        orders.append({
            "orderId": f"ORD{i + 100001}",
            "customerId": f"CUST{random.randint(1000, 9999)}",
            "amount": round(random.uniform(100, 50000), 2),
            "createdAt": created.isoformat()
        })

    # Inject duplicate-order examples:
    for i in range(100):
        original = orders[i].copy()
        original["orderId"] = f"ORD{150001 + i}"

        original_time = datetime.fromisoformat(
            original["createdAt"]
        )
        original_time = original_time.replace(
            second=(original_time.second + 20) % 60
        )
        original["createdAt"] = original_time.isoformat()

        orders.append(original)

    save_csv(
        "Set_1_Retail_Order",
        "orders.csv",
        ["orderId", "customerId", "amount", "createdAt"],
        orders
    )


# --------------------------------------------------
# SET 2: RETAIL BANKING
# --------------------------------------------------

def generate_transactions():
    transactions = []
    start = datetime(2026, 10, 1, 0, 0, 0)
    merchants = [
        "Amazon", "Flipkart", "Walmart",
        "Reliance", "BigBasket", "Swiggy"
    ]

    for i in range(100000):
        posted = start + timedelta(
            seconds=random.randint(0, 30 * 24 * 60 * 60)
        )

        transactions.append({
            "transactionId": f"TXN{i + 100001:06d}",
            "accountId": f"ACC{random.randint(1000, 9999)}",
            "amount": round(random.uniform(10, 100000), 2),
            "merchant": random.choice(merchants),
            "postingDate": posted.isoformat()
        })

    # Inject duplicate posting examples:
    for i in range(100):
        original = transactions[i].copy()
        original["transactionId"] = f"TXN{200001 + i:06d}"

        original_time = datetime.fromisoformat(
            original["postingDate"]
        )
        original["postingDate"] = (
            original_time + timedelta(seconds=30)
        ).isoformat()

        transactions.append(original)

    save_csv(
        "Set_2_Retail_Banking",
        "transactions.csv",
        [
            "transactionId", "accountId",
            "amount", "merchant", "postingDate"
        ],
        transactions
    )


# --------------------------------------------------
# SET 3: HOSPITAL APPOINTMENT DESK
# --------------------------------------------------

def generate_hospital_data():
    patients = []

    for i in range(20000):
        patients.append({
            "patientId": f"PAT{i + 100001}",
            "patientName": f"Patient_{i + 1}",
            "age": random.randint(1, 90),
            "phone": f"9{random.randint(100000000, 999999999)}"
        })

    save_csv(
        "Set_3_Hospital",
        "patients.csv",
        ["patientId", "patientName", "age", "phone"],
        patients
    )

    appointments = []
    start = datetime(2026, 10, 15, 8, 0, 0)

    for i in range(5000):
        arrival = start + timedelta(
            minutes=random.randint(0, 30 * 24 * 60)
        )

        slot = arrival.replace(
            minute=(arrival.minute // 15) * 15,
            second=0,
            microsecond=0
        )

        appointments.append({
            "appointmentId": f"APT{i + 1:05d}",
            "patientId": random.choice(patients)["patientId"],
            "urgency": random.randint(1, 5),
            "arrivalTime": arrival.isoformat(),
            "slot": slot.isoformat()
        })

    # Inject double-booked appointment examples:
    for i in range(50):
        original = appointments[i].copy()
        original["appointmentId"] = f"APT{5001 + i:05d}"
        appointments.append(original)

    save_csv(
        "Set_3_Hospital",
        "appointments.csv",
        [
            "appointmentId", "patientId",
            "urgency", "arrivalTime", "slot"
        ],
        appointments
    )


# --------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    print("GENERATING HEXAWARE ASSIGNMENT DATASETS")
    print("-" * 45)

    generate_orders()
    generate_transactions()
    generate_hospital_data()

    print("-" * 45)
    print("ALL DATASETS GENERATED SUCCESSFULLY!")

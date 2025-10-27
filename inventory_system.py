import json
import logging
from datetime import datetime
from json import JSONDecodeError

# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """Add quantity to an item, creating it if missing."""
    if logs is None:
        logs = []

    # basic input validation
    if not isinstance(item, str) or not item.strip():
        logging.warning("Invalid item name: %r", item)
        return
    if not isinstance(qty, int):
        logging.warning("Invalid qty (not int): %r", qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def removeItem(item, qty):
    """Remove quantity; delete item if quantity becomes <= 0."""
    try:
        if not isinstance(item, str) or not isinstance(qty, int):
            raise TypeError("removeItem expects (str, int)")
        current = stock_data.get(item)
        if current is None:
            raise KeyError(item)
        new_qty = current - qty
        if new_qty <= 0:
            del stock_data[item]
        else:
            stock_data[item] = new_qty
    except KeyError:
        logging.info("Tried to remove from missing item: %r", item)
    except (TypeError, ValueError) as e:
        logging.error("Bad input to removeItem: %s", e)


def getQty(item):
    """Return quantity; 0 if item is missing."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load inventory from JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.info("No %s found; starting with empty inventory.", file)
        stock_data = {}
    except JSONDecodeError as e:
        logging.error("Invalid JSON in %s: %s", file, e)
        stock_data = {}


def saveData(file="inventory.json"):
    """Save inventory to JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        logging.error("Failed to write %s: %s", file, e)


def printData():
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def checkLowItems(threshold=5):
    return [i for i, q in stock_data.items() if q < threshold]


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    addItem("apple", 10)
    addItem("banana", 2)
    addItem(123, "ten")  # invalid types; will be logged & ignored
    removeItem("apple", 3)
    removeItem("orange", 1)

    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")

    saveData()
    loadData()
    printData()
    print("Eval removed for security reasons")


if __name__ == "__main__":
    main()

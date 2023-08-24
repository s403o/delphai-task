#!/usr/bin/env python3
import sys
import subprocess
from pymongo import MongoClient

def main():
    # Extract MongoDB connection string from the command line argument
    mongodb_uri = sys.argv[1]

    # Extract the secondary node hostname from the MongoDB URI
    secondary_hostname = mongodb_uri.split('@')[1].split('/')[0]

    # Connect to the secondary node and issue the fsyncLock command
    mongo_client = MongoClient(mongodb_uri)
    admin_db = mongo_client.get_database('admin')
    admin_db.command('fsyncLock')

    # Make a VM snapshot for the provided secondary node hostname
    subprocess.run(['make-vm-snapshot', secondary_hostname])

    # Connect to the secondary node and issue the fsyncUnlock command
    admin_db.command('fsyncUnlock')

if __name__ == "__main__":
    main()


# main.py
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.auto.gethdev import w3 as w4
from web3.middleware import construct_sign_and_send_raw_middleware


# Setup
#alchemy_url = "https://polygon-mumbai.g.alchemy.com/v2/EfYlAW1aOD8rm-GOPC81499C1ZulKiVn"
alchemy_url = "https://gateway.tenderly.co/public/polygon-mumbai"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
private_key = "45f26a1e5a2d50bd7c905c0446386acf9ca77da632cca16d52e1922da3ec1aa0"
# Print if web3 is successfully connected
abi = """
  [
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "patientAddress",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "name",
          +-
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "familyHistory",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "genotype",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "bloodGroup",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "allergy",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "medicalHistory",
          "type": "string"
        }
      ],
      "name": "addPatient",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "patientAddress",
          "type": "address"
        }
      ],
      "name": "deletePatient",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "patientAddress",
          "type": "address"
        }
      ],
      "name": "getPatient",
      "outputs": [
        {
          "components": [
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "familyHistory",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "genotype",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "bloodGroup",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "allergy",
              "type": "string"
            },
            {
              "internalType": "string",
              "name": "medicalHistory",
              "type": "string"
            }
          ],
          "internalType": "struct MedicalRecords.Patient",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "patients",
      "outputs": [
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "familyHistory",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "genotype",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "bloodGroup",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "allergy",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "medicalHistory",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "patientAddress",
          "type": "address"
        },
        {
          "internalType": "string",
          "name": "name",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "familyHistory",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "genotype",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "bloodGroup",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "allergy",
          "type": "string"
        },
        {
          "internalType": "string",
          "name": "medicalHistory",
          "type": "string"
        }
      ],
      "name": "updatePatient",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]
  """
print(w3.is_connected())
acct = w3.eth.account.from_key(private_key)
w3.eth.default_account = acct.address
address = "0x9e37C395db81F58a9D0B5e21892bd422207CA614"
# 0xFE970F2a317C7bFD5887292B196661A7325b9F2d
# 0x722a62D34E46460CB1DaFdc58AdCA70474af578C
w3.middleware_onion.add(
    construct_sign_and_send_raw_middleware(acct))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=address, abi=abi)
d = contract.all_functions()
print(d)
# print a list of the accounts present in alchemy
print(w3.eth.accounts)
# exit(0)
# print(w4.client_version)
# exit(0)
# Example function calls

# Add a new allergy for a patient


def add_patient(patient_address, name, family_history, genotype, blood_group, allergy, medical_history):
    transaction = contract.functions.addPatient(
        patient_address, name, family_history, genotype, blood_group, allergy, medical_history).transact()
    import time
    # time.sleep(30)
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction)
    return transaction_receipt


def get_patient(patient_address):
    data = contract.functions.getPatient(patient_address).call()
    print(data)
    return data


def update_patient(patient_adress, name, family_history, genotype, blood_group, allergy, medical_history):
    txn_hash = contract.functions.updatePatient(
        patient_adress, name, family_history, genotype, blood_group, allergy, medical_history
    ).transact()

    # Wait for the transaction to be mined
    w3.eth.wait_for_transaction_receipt(txn_hash)


def delete_patient(patient_adress):
    txn_hash = contract.functions.deletePatient(patient_adress).transact()

    # Wait for the transaction to be mined
    w3.eth.wait_for_transaction_receipt(txn_hash)


# Example usage
    """
add_patient("John Doe", "No family history", "AA", "O+",
            "None", "No significant medical history")
print("Patient information:", get_patient())

update_patient("John Doe", "No family history", "AA", "O+",
               "Pollen allergy", "No significant medical history")
print("Updated patient information:", get_patient())

delete_patient()
print("Patient information after deletion:", get_patient())

# Example usage
patient_address = "0xbf8b66efDc0555E4Cf402780184e18951a6FDB08"
allergy_name = "Peanuts"
severity = "High"
"""

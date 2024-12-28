# Certificate Validation using Blockchain

## Introduction

The system comprises of 2 main entities:
- **Institute**: Responsible for generating and issuing certificates. Has the functionality to generate and view certificates.

- **Verifier**: Responsible for verifying certificates. Has the functionality to verify certificates by either uploading a certificate pdf or by inputting the certificate id.

---

## Features

- **Smart Contract:** Utilizes a Solidity smart contract to manage and store certificate details on the Ethereum blockchain.
- **IPFS Integration:** Stores certificate PDFs on IPFS via IPFS Desktop for decentralized and secure file storage.
- **Streamlit App:** Provides a user-friendly interface for generating and verifying certificates.

---

## Getting Started

Clone the repository using the command:
```sh
git clone https://github.com/salahdardour77/blockchain.git

```
### Prerequisites

- **Node version >= 21.0.0**  
Truffle requires node version 16 or higher. The node version on my machine on which I tested this project was 21.0.0. You can try a lower node version (>=16.0).

- **Python version >= 3.9.10**  
    Python version 3.9.10 or higher is recommended but other versions may also work.

- **Globally installed packages for Truffle and Ganache-cli**  

    ```sh
    npm install -g truffle
    ```
    ```sh
    npm install -g ganache-cli
    ```

- **Python packages**  
    In the project's root directory, exececute the command:
    ```sh
    pip install -r application/requirements.txt
    ```
    It is recommended to create a virtual environment and then install the requirements and run the streamlit application in that virtual environment.

- **IPFS setup**  
    Download the IPFS desktop application from this link: https://docs.ipfs.tech/install/ipfs-desktop/
- **.env file**  
    Finally your .env file should look like:

    ```sh
    institute_email = "institute@gmail.com" # Feel free to modify this
    institute_password = "123456" # Feel free to modify this
    ```
    however, you can modify this file with your coresponding needs.
### Running the project

1. Open a terminal anywhere and start the Ganache blockchain.
    ```
    ganache-cli -h 127.0.0.1 -p 8545
    ```

2. Open a new terminal in the project's root directory and execute the following command to compile and deploy the smart contracts.
    ```sh
    truffle migrate
    ```

3. Change the working directory to application directory inside the project's root directory.
    ```sh
    cd app
    ```

4. Launch the streamlit app.
    ```sh
    streamlit run main.py
    ```

5. You can now view the app on your browser running on [localhost:8501](https:localhost:8501).

6. To stop the application, press Ctrl+C.

---
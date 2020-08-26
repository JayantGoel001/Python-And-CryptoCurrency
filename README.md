# Python And CryptoCurrency

A cryptocurrency (or crypto currency) is a digital asset designed to work as a medium of exchange wherein individual coin ownership records are stored in a ledger existing in a form of computerized database using strong cryptography to secure transaction records, to control the creation of additional coins, and to verify the transfer of coin ownership. It typically does not exist in physical form (like paper money) and is typically not issued by a central authority. Cryptocurrencies typically use decentralized control as opposed to centralized digital currency and central banking systems. When a cryptocurrency is minted or created prior to issuance or issued by a single issuer, it is generally considered centralized. When implemented with decentralized control, each cryptocurrency works through distributed ledger technology, typically a blockchain, that serves as a public financial transaction database.

Bitcoin, first released as open-source software in 2009, is the first decentralized cryptocurrency. Since the release of bitcoin, over 6,000 altcoins (alternative variants of bitcoin, or other cryptocurrencies) have been created.

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/cryptocurrency.jpg)

## History

In 1983, the American cryptographer David Chaum conceived an anonymous cryptographic electronic money called ecash. Later, in 1995, he implemented it through Digicash,an early form of cryptographic electronic payments which required user software in order to withdraw notes from a bank and designate specific encrypted keys before it can be sent to a recipient. This allowed the digital currency to be untraceable by the issuing bank, the government, or any third party.

In 1996, the National Security Agency published a paper entitled How to Make a Mint: the Cryptography of Anonymous Electronic Cash, describing a Cryptocurrency system, first publishing it in an MIT mailing list and later in 1997, in The American Law Review (Vol. 46, Issue 4).

In 1998, Wei Dai published a description of "b-money", characterized as an anonymous, distributed electronic cash system. Shortly thereafter, Nick Szabo described bit gold. Like bitcoin and other cryptocurrencies that would follow it, bit gold (not to be confused with the later gold-based exchange, BitGold) was described as an electronic currency system which required users to complete a proof of work function with solutions being cryptographically put together and published.

The first decentralized cryptocurrency, bitcoin, was created in 2009 by presumably pseudonymous developer Satoshi Nakamoto. It used SHA-256, a cryptographic hash function, as its proof-of-work scheme. In April 2011, Namecoin was created as an attempt at forming a decentralized DNS, which would make internet censorship very difficult. Soon after, in October 2011, Litecoin was released. It was the first successful cryptocurrency to use scrypt as its hash function instead of SHA-256. Another notable cryptocurrency, Peercoin was the first to use a proof-of-work/proof-of-stake hybrid.

On 6 August 2014, the UK announced its Treasury had been commissioned a study of cryptocurrencies, and what role, if any, they can play in the UK economy. The study was also to report on whether regulation should be considered.

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/bitcoin.jpg)

## Architecture

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/arch.jpg)

Decentralized cryptocurrency is produced by the entire cryptocurrency system collectively, at a rate which is defined when the system is created and which is publicly known. In centralized banking and economic systems such as the Federal Reserve System, corporate boards or governments control the supply of currency by printing units of fiat money or demanding additions to digital banking ledgers. In the case of decentralized cryptocurrency, companies or governments cannot produce new units, and have not so far provided backing for other firms, banks or corporate entities which hold asset value measured in it. The underlying technical system upon which decentralized cryptocurrencies are based was created by the group or individual known as Satoshi Nakamoto.

As of May 2018, over 1,800 cryptocurrency specifications existed. Within a cryptocurrency system, the safety, integrity and balance of ledgers is maintained by a community of mutually distrustful parties referred to as miners: who use their computers to help validate and timestamp transactions, adding them to the ledger in accordance with a particular timestamping scheme.

Most cryptocurrencies are designed to gradually decrease production of that currency, placing a cap on the total amount of that currency that will ever be in circulation. Compared with ordinary currencies held by financial institutions or kept as cash on hand, cryptocurrencies can be more difficult for seizure by law enforcement. This difficulty is derived from leveraging cryptographic technologies.

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/blockchain2.jpg)

### Blockchain

The validity of each cryptocurrency's coins is provided by a blockchain. A blockchain is a continuously growing list of records, called blocks, which are linked and secured using cryptography. Each block typically contains a hash pointer as a link to a previous block, a timestamp and transaction data. By design, blockchains are inherently resistant to modification of the data. It is "an open, distributed ledger that can record transactions between two parties efficiently and in a verifiable and permanent way". For use as a distributed ledger, a blockchain is typically managed by a peer-to-peer network collectively adhering to a protocol for validating new blocks. Once recorded, the data in any given block cannot be altered retroactively without the alteration of all subsequent blocks, which requires collusion of the network majority.

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/blockchain.jpg)

Blockchains are secure by design and are an example of a distributed computing system with high Byzantine fault tolerance. Decentralized consensus has therefore been achieved with a blockchain. The public nature of the blockchain ledger protects the integrity of whatever is being transacted since no one entity owns the database. The added work required to solve the encryption in a proof-of-stake system ensures that the public ledger is not modified at random, thus solving the double-spending problem without the need of a trusted authority or central server to administer the database, assuming no 51% attack (that has worked against several cryptocurrencies).

### Timestamping
Cryptocurrencies use various timestamping schemes to "prove" the validity of transactions added to the blockchain ledger without the need for a trusted third party.

The first timestamping scheme invented was the proof-of-work scheme. The most widely used proof-of-work schemes are based on SHA-256 and scrypt.

Some other hashing algorithms that are used for proof-of-work include CryptoNight, Blake, SHA-3, and X11.

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/timestamp.png)

The proof-of-stake is a method of securing a cryptocurrency network and achieving distributed consensus through requesting users to show ownership of a certain amount of currency. It is different from proof-of-work systems that run difficult hashing algorithms to validate electronic transactions. The scheme is largely dependent on the coin, and there's currently no standard form of it. Some cryptocurrencies use a combined proof-of-work and proof-of-stake scheme.

### Mining

In cryptocurrency networks, mining is a validation of transactions. For this effort, successful miners obtain new cryptocurrency as a reward. The reward decreases transaction fees by creating a complementary incentive to contribute to the processing power of the network. The rate of generating hashes, which validate any transaction, has been increased by the use of specialized machines such as FPGAs and ASICs running complex hashing algorithms like SHA-256 and Scrypt. This arms race for cheaper-yet-efficient machines has existed since the day the first cryptocurrency, bitcoin, was introduced in 2009. With more people venturing into the world of virtual currency, generating hashes for this validation has become far more complex over the years, with miners having to invest large sums of money on employing multiple high performance ASICs. Thus the value of the currency obtained for finding a hash often does not justify the amount of money spent on setting up the machines, the cooling facilities to overcome the heat they produce, and the electricity required to run them. As of July 2019, bitcoin's electricity consumption is estimated to about 7 gigawatts, 0.2% of the global total, or equivalent to that of Switzerland.

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/mining.jpg)

Some miners pool resources, sharing their processing power over a network to split the reward equally, according to the amount of work they contributed to the probability of finding a block. A "share" is awarded to members of the mining pool who present a valid partial proof-of-work.

As of February 2018, the Chinese Government halted trading of virtual currency, banned initial coin offerings and shut down mining. Some Chinese miners have since relocated to Canada. One company is operating data centers for mining operations at Canadian oil and gas field sites, due to low gas prices. In June 2018, Hydro Quebec proposed to the provincial government to allocate 500 MW to crypto companies for mining. According to a February 2018 report from Fortune, Iceland has become a haven for cryptocurrency miners in part because of its cheap electricity.

In March 2018, the city of Plattsburgh in upstate New York put an 18-month moratorium on all cryptocurrency mining in an effort to preserve natural resources and the "character and direction" of the city.

### GPU price rise

An increase in cryptocurrency mining increased the demand for graphics cards (GPU) in 2017. (The computing power of GPUs makes them well-suited to generating hashes.) Popular favorites of cryptocurrency miners such as Nvidia's GTX 1060 and GTX 1070 graphics cards, as well as AMD's RX 570 and RX 580 GPUs, doubled or tripled in price – or were out of stock. A GTX 1070 Ti which was released at a price of $450 sold for as much as $1100. Another popular card GTX 1060's 6 GB model was released at an MSRP of $250, sold for almost $500. RX 570 and RX 580 cards from AMD were out of stock for almost a year. Miners regularly buy up the entire stock of new GPU's as soon as they are available.

Nvidia has asked retailers to do what they can when it comes to selling GPUs to gamers instead of miners. "Gamers come first for Nvidia," said Boris Böhles, PR manager for Nvidia in the German region.

### Wallets

![](https://github.com/CormacKrum/Python-And-CryptoCurrency/blob/master/wallet.png)
*An example paper printable bitcoin wallet consisting of one bitcoin address for receiving and the corresponding private key for spending.*

A cryptocurrency wallet stores the public and private "keys" or "addresses" which can be used to receive or spend the cryptocurrency. With the private key, it is possible to write in the public ledger, effectively spending the associated cryptocurrency. With the public key, it is possible for others to send currency to the wallet.


### Anonymity

Bitcoin is pseudonymous rather than anonymous in that the cryptocurrency within a wallet is not tied to people, but rather to one or more specific keys (or "addresses"). Thereby, bitcoin owners are not identifiable, but all transactions are publicly available in the blockchain. Still, cryptocurrency exchanges are often required by law to collect the personal information of their users.

Additions such as Zerocoin, Zerocash and CryptoNote have been suggested, which would allow for additional anonymity and fungibility.

### Fungibility

Most cryptocurrency tokens are fungible and interchangeable. However, unique non-fungible tokens also exist. Such tokens can serve as assets in games like CryptoKitties.

***
<code><img height="70px" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/ethereum/ethereum.png"></code>
<code><img height="70px" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bitcoin/bitcoin.png"></code>
<code><img height="70px" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/monero/monero.png"></code>

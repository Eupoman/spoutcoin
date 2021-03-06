# Spoutcoin
The project is for a website that allows the user to designate benefactors to receive their cryptocurrency (Bitcoin, Ethereum, Monero, Litecoin, etc) on death. For the purposes of this MVP, I created a fake persona to act as the user.

The fake persona user has Twitter, Facebook and Reddit accounts. If the user has not posted with X days, the system designates this user as 'dead' and notifies the benefactors. These benefactors have a combination of Twitter, LinkedIn, and/or email accounts assigned to them -- they are notified through one or more of these services that the persona has died and they are eligible to receive funds and directed to login to the website.

The benefactor is directed to sign-up on the website to check eligibility. This is handled through LinkedIn, Twitter, and/or email. If LinkedIn or Twitter are used for sign-up/login, this is handled through their respective APIs. They are also required to complete a 2FA process through Twilio or Google Authenticator for setup as it is required for subsequent logins.

Once they are logged in, they are directed to the page of the fake persona. It displays the persona's name, last known social media activity, and a video message to play. For the purposes of this MVP, I just used machine learning with listed Q/A. Once they are detected as real benefactors, it displays the fake persona's name, the total amount of cryptocurrency being left to benefactors, the total number of benefactors, and the directions for disbursement. For the purposes of this MVP, I used Ethereum as it has the most readily available methods of interaction.

For ETH transaction, web3.py was used.
https://github.com/pipermerriam/web3.py

The user is directed to input their requested reason disbursement. The system checks this reason against training data to give a binary "yes" or "no" response from a data standpoint. From a user standpoint, the yes or no response displays a random statement from a respective list of yes, or no answers. If the response is yes, the system disburses an amount equal to the one divided by the total amount of benefactors to the user's designated Ethereum address. If there is 40 ETH available and 20 benefactors, then each benefactors are able to receive 2 ETH if they get a yes response. If they receive a no response, it allows them 4 more attempts before a 6-hour wait period is enacted. This is merely to prevent spamming attempts. The user is notified of this wait time before the first input, each attempt warns them of how many attempts are left, and once the wait time is enacted, a countdown occurs.

The training data consists of a list of Questions and Answers to mimic whether or not the persona would have approved this type of transaction. The training data was used in several text format (CSV, JSON, etc).

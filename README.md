# Ban-evasion handling
A tool for detecting and preventing ban evasion on an IRC channel.

## Here's how it works:
1. The script keeps track of user information in a dictionary called `user_data`. The dictionary is initialized as an empty dictionary at the beginning of the script.
2. When a user connects to the IRC channel and performs a `WHOIS` query (a command that retrieves information about a user), the whois_cb function is called. This function extracts the user's `nickname`, `hostname`, and `real name` from the WHOIS response and updates the user_data dictionary with this information using the `update_user_data` function.
3. The `ban_evasion_detected` function is called to check if a user is attempting to evade a ban. This function loops through all the users in the user_data dictionary and checks if any user has the same hostname as the user being checked but a different nickname. If such a user is found, it is assumed that the user has changed their nickname to evade a ban, and the function bans the user using the `/ban` IRC command.

This script could be useful for preventing users from evading bans on an IRC channel. 

## Potential concerns to consider:

1. False positives: The script relies on hostname information to detect ban evasion. In some cases, multiple users may share the same hostname (for example, if they are all connecting from the same organization), which could lead to false positives and innocent users being banned.
2. Privacy concerns: The script collects and stores user information (hostname and real name) without explicit user consent. Depending on the context, this could be seen as a violation of privacy.
3. Performance issues: The script may become slow or unresponsive if the user_data dictionary becomes very large, particularly if there are many users connecting to the IRC channel.

It's important to consider the potential benefits and drawbacks of using this script in the context of your specific use case, and to be transparent with users about how their data is being used.

## IRC Meta

### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Deprecated. Extract video information from a YouTube URL and post it back to the channel. (Python)
- [weechat.youtube-api](https://github.com/apple-fritter/weechat.youtube-api): Extract video information from a YouTube URL and post it back to the channel. (Python)

### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

### Other
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)
- [scrimshaw](https://github.com/apple-fritter/scrimshaw): Create a quoteslist of any given user, from your driftwood formatted logs. (Rust)

### IRC usage considerations
When working with any project involving IRC (Internet Relay Chat), it's important to keep the following considerations in mind to ensure a positive and respectful environment for all participants.

#### Philosophy of Use
Tailor your project's behavior and responses to align with the expected norms and conventions of IRC. Take into account the preferences and expectations of IRC users, ensuring that your project provides a seamless and familiar experience within the IRC ecosystem.

#### Foster a Positive and Inclusive Environment
Respect and adhere to the guidelines and policies of the IRC platform you are using. Familiarize yourself with the platform's rules regarding script usage, automation, and acceptable behavior. Comply with the platform's Terms of Service, and be mindful of any limitations or restrictions imposed by the platform. Strive to create an inclusive and welcoming environment where all users can engage respectfully and comfortably.

#### Respect the Rights and Dignity of Other Users
Maintain a polite and courteous demeanor in all interactions. Uphold the fundamental principles of respect, avoiding engagement in illegal, inappropriate, or offensive behavior. This includes refraining from using derogatory or inflammatory language, sharing explicit, triggering, or offensive content, engaging in harassment, or launching personal attacks. Obtain explicit consent before interacting with other users or sending automated responses. Respect the privacy of other users and avoid invading their personal space without their permission.

#### Respect the IRC Community and Channels
Avoid disrupting the normal flow of conversation within IRC channels. Ensure that your project's actions and responses do not cause unnecessary disruptions or inconvenience to other users. Implement mechanisms to prevent spamming or flooding the channel with excessive or irrelevant messages. Handle errors gracefully, preventing unintended behavior or disruptions to the IRC platform or the experiences of other users.

#### Ensure Compatibility
Consider the potential variations in behavior across different IRC platforms and clients. While aiming for compatibility, be aware that certain functionalities may not be available or consistent across all platforms. Test your project on multiple IRC platforms and clients to ensure compatibility and provide the best possible experience for users.

---

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

---

## License

These files released under the [MIT License](LICENSE).

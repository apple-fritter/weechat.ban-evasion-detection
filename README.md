# weechat.ban-evasion-detection
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

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).

import weechat

# Keep track of user information in a dictionary
user_data = {}

def update_user_data(nick, host, realname):
    user_data[nick] = {"host": host, "realname": realname}

def ban_evasion_detected(nick):
    # Check if user has changed nicks
    for existing_nick, data in user_data.items():
        if existing_nick != nick and data["host"] == user_data[nick]["host"]:
            # Ban user
            weechat.command("", "/ban {0}".format(user_data[nick]["host"]))
            return True
    return False

def whois_cb(data, buffer, date, tags, displayed, highlight, prefix, message):
    # Extract information from whois response
    nick = prefix.split("!")[0]
    host = message.split(" ")[0].split("@")[1]
    realname = " ".join(message.split(" ")[2:]).strip()
    # Update user information
    update_user_data(nick, host, realname)
    # Check for ban evasion
    ban_evasion_detected(nick)
    return weechat.WEECHAT_RC_OK

# Hook whois response
weechat.hook_print("", "", "313", 1, "whois_cb", "")


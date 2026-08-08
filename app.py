import os

from dotenv import load_dotenv

import ldclient
from ldclient import Context
from ldclient.config import Config


# Load variables from .env
load_dotenv()

# Get LaunchDarkly SDK key
sdk_key = os.getenv("LD_SDK_KEY")

if not sdk_key:
    raise ValueError("LD_SDK_KEY is not configured")


# Configure LaunchDarkly: configures the LaunchDarkly SDK.
ldclient.set_config(Config(sdk_key))

# Get LaunchDarkly client: Think of client as My Python application's connection/interface to LaunchDarkly.
client = ldclient.get()

# Check connection
if not client.is_initialized():
    raise RuntimeError("LaunchDarkly client failed to initialize")


# Create user/context
ajit_context = Context.builder("ajit").name("ajit rawat").build()
sushil_context = Context.builder("sushil").name("Sushil").build()



# Evaluate feature flag
show_new_dashboard = client.variation(
    "new-dashboard", #This is the flag key.It must match the flag in LaunchDarkly.
    ajit_context,#The context for which the flag is being evaluated. In this case, it's the user "sushil".
    False #Default value if the flag is not found or if there is an error
)


# Application behavior based on the feature flag status.
# If the feature flag "new-dashboard" is enabled, show the new dashboard; otherwise, show the old dashboard
if show_new_dashboard:
    print("================================")
    print("Welcome to NEW Employee Dashboard")
    print("================================")
else:
    print("================================")
    print("Welcome to OLD Employee Dashboard")
    print("================================")
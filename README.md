
# UStore

A simple library for the managment/usage for users

## Getting Started

### Installing

```
pip install ustore
```

### Example

```
import ustore
ustore.init(".")               # Set user storage location to current dir
register_account("foo","bar")  # Make a user with the username foo and a password bar
setconfig("foo","data","bar")  # Set the config value for the user foo to data
getconfig("foo","bar)          # Get the config for the user foo
valid_password("foo","pass")   # Check if the user foo's password is pass
```

### Documentation

```
ustore.init(".") 
```

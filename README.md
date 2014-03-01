# Description

Run scripts on network state changes

# Install

    pip install connman-dispatcher [--user]


# Usage

    $ connman-dispatcher -h
    usage: connman-dispatcher [-h] -p PATH

Scripts are run from folders setted in -p argument
One can set more than one folder.

When network state changes, each script is executed with either 'up' or 'down'
argument, depening on the current network state.

For example, if connman-dispatcher was run like this:

    connman-dispatcher -p /etc/connman-dispatcher

And we have some scripts in bash in this folder, something like:

```bash
up() {
# handle up state
}

down() {
# handle down state
}

state="$1"

case $state in
    up)
        up
        ;;
    down)
        down
        ;;
esac
```

When network state changes from 'down' to 'up', each script in '/etc/connman-dispatcher'
will be executed with 'up' argument, like this:

    /etc/connman-dispatcher/10_handle_network_state_change.sh up
    /etc/connman-dispatcher/some_other_executable up


Scripts, as well as script folders are sorted by name.


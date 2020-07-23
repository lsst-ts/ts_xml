##################
Non XML SAL Topics
##################

Private Fields
==============

private_sndStamp (TAI, unix seconds)
    Time at which the sample was sent.
private_rcvStamp (TAI, unix seconds)
    Time at which sample was received.
private_identity
    For a CSC this has the form <SAL component name>[:index] e.g. "Script:5" or "ATDome".
    For a user this has the form username@host.
    This field is used for authorization.
    New in ts_sal 4.2.
private_origin
    The process ID of the writer.
private_host
    The host address of the writer.
    This is deprecated, and due to be removed in ts_sal 5.
private_seqNum
    For commands this uniquely identifies the command (within a reasonable timespan, since the value must eventually wrap around).
    For other kinds of topics this may be incremented for each sample, though that is optional.
<SAL component name>ID (ATDomeID)
    Only present for indexed SAL components.
    The SAL index of the writer.

Non XML Topics
==============

ackcmd
------

private_seqNum
    The private_seqNum of the command being acknowledged.
ack
    The acknowledgement code, one of CMD\_ constants, such as CMD_COMPLETE = 303 or CMD_FAILED = -302.
error
    The error code.
    Set to a nonzero value if ack=CMD_FAILED.
result
    Salobj sets this to an error message if ack=CMD_FAILED.
identity
    The private_identity of the command being acknowledged (see below).
host
    The private_host of the command being acknowledged.
    private_host is deprecated, so this field is also deprecated, and both should be gone in ts_sal 5.
origin
    The private_origin of the command being acknowledged, which is a process ID.
cmdtype
    An index of all alphabetical topics inside of the component.
timeout
    The approximate expected duration of the command.
    Only set if ack=CMD_INPROGRESS.

Acknowledgement Sequence
========================
The initial ack code is CMD_ACK when the command is read.
If the command will take a long time to run then the CSC should respond with a CMD_INPROGRESS ack that includes an estimate of the command duration.
This should only happen after the command has been approved
Usually the next ack is the final one for this command and is typically one of:

* CMD_COMPLETE if the command finishes successfully.
* CMD_FAILED if the commands fails.
* CMD_NOPERM if the command issuer is not authorized to send the command
* CMD_ABORTED if the command is superseded

CMD_TIMEOUT is returned if the command *issuer* times out waiting for command completion.
Note that it is the issuer, not the CSC, that returns this.
If the command times out inside the CSC then the ack code is CMD_FAILED.
In particular note that if the issuer gives up waiting for command completion and then the command finishes, the user will only see the CMD_TIMEOUT ack, but the DDS system will see the final ack from the CSC.
There are at least two other CMD\_ codes as well:

* CMD_NOACK: ts_salobj sets the ackcmd filed of AckTimeoutError to this value if no CMD_ACK was seen for the command before the command timed out.
* CMD_STALLED: Indicates a command has slowed down unexpectedly but is still working on it.

Neuropixels data collected with spikeglx (very common in the building) has a fixed
output format that should not be changed.

Anything in the 'myname' section is prepended to the output by the software. The
g0, t0 and imec0 suffixes are required for proper operation of downstream software.

Therefore, we can change myname (this is analagous to choosing a name for the 
subject when running spikeglx), but g0, g0, imec0 should not be changed.
How does this complicate BIDS?

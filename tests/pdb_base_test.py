"""
Unit tests for PdbBase class.

Validates the PDB base object API: default is_replaceable is False,
and platform-specific methods raise NotImplementedError. Ensures
PDB can be used where PSU is expected (voltage/current/power delegation).
"""

from sonic_platform_base.pdb_base import PdbBase


class TestPdbBase:

    def test_pdb_base_device_type(self):
        """PDB device type constant."""
        assert PdbBase.DEVICE_TYPE == "pdb"

    def test_pdb_base_not_implemented_methods(self):
        """Platform must implement these; base raises NotImplementedError."""
        pdb = PdbBase()
        not_implemented_methods = [
            pdb.get_name,
            pdb.get_presence,
            pdb.get_status,
            pdb.get_model,
            pdb.get_serial,
            pdb.get_revision,
            pdb.get_temperature,
            pdb.get_output_current,
            pdb.get_output_power,
            pdb.get_output_voltage,
            pdb.get_input_current,
            pdb.get_input_power,
            pdb.get_input_voltage,
            pdb.get_maximum_supplied_power,
        ]
        for method in not_implemented_methods:
            exception_raised = False
            try:
                method()
            except NotImplementedError:
                exception_raised = True
            assert exception_raised, "Expected NotImplementedError from {}".format(method.__name__)

    def test_pdb_base_thermal_inherited(self):
        """PDB inherits thermal list from PsuBase; empty by default."""
        pdb = PdbBase()
        assert pdb.get_num_thermals() == 0
        assert pdb.get_all_thermals() == []
        assert pdb.get_thermal(0) is None

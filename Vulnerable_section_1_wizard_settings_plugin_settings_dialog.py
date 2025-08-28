 from pymol.Qt import QtWidgets
 
 from .settings_gui import Ui_Form
 from molecular_dynamics.simulation_params import SimulationParameters
 
 plugin_root = Path(__file__).parent
     yaml_str = raw_yaml.decode("utf-8")
     params.parse_yaml(yaml_str)
 
    print(f"Loaded configuration from {CONFIG_PATH}")
 
     return params
 
 
 def save_configuration(params):
    params.serialize(CONFIG_PATH)
    print(f"Saved configuration to {CONFIG_PATH}")
 
 
 def get_force_field_choices():
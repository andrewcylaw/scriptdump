import os
import configparser
import argparse
from datetime import datetime
from subprocess import call

desc = """Handy Python script that runs prboom[-plus] with preset configs.
       See usage.txt for more details on running the script and loading properties."""

# Parse script args - config file location + custom config tag
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-i', '--ini', nargs=1, help="ini file", required=True)
parser.add_argument('-c', '--custom_config', nargs=1, help="custom config tag", required=True)

custom_config_tag = vars(parser.parse_args())['custom_config'][0]
conf_file_loc = vars(parser.parse_args())['ini'][0]

if(not os.path.exists(conf_file_loc) or not os.path.isfile(conf_file_loc)):
	print("\terror: cannot find ini config file: " + conf_file_loc)
	exit(0)

config = configparser.ConfigParser()
config.read(conf_file_loc)

# Parse [meta-config] tags
if('prboom-location' not in config['meta-config'] or 'iwad-location' not in config['meta-config']):
	print("\terror: missing 'iwad-location' and/or 'prboom-location' in .ini config file")
	exit(0)

prboom_location = config['meta-config']['prboom-location']
iwad_location = config['meta-config']['iwad-location']

if(not os.path.exists(prboom_location) 
	or not os.path.isfile(prboom_location)
	or not os.access(prboom_location, os.X_OK)):
	print("\terror: prboom executable location not an exe or not found: " + prboom_location)
	exit(0)

if(not os.path.exists(iwad_location)
	or not os.path.isdir(iwad_location)):
	print("\terror: iwad location not a directory or does not exist: " + iwad_location)
	exit(0)

if(custom_config_tag not in config.sections()):
	print("\terror: cannot find custom properties tagged: " + custom_config_tag)
	exit(0)

demo_suffix = "_" + datetime.now().strftime("%y%m%d_t%H%M") if config['meta-config']['timestamp'] else ""


# [prboom-config] globals and override configs from the custom tag
prboom_config = config['prboom-config']
loaded_config = config[custom_config_tag]

for conf in loaded_config:
	prboom_config[conf] = loaded_config[conf]

if("record" in prboom_config):
	prboom_config["record"] = prboom_config["record"] + demo_suffix


# Construct prboom executable command & run
final_run = "{} -iwad {} ".format(prboom_location, iwad_location)

for i in prboom_config:
	final_run = "{} -{} {}".format(final_run, i, prboom_config[i])

print(final_run)
call(final_run)

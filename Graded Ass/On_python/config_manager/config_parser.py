import configparser
import os
from db_setup import db, ConfigData, app

# This function parses a configuration file and stores its sections and data in the database.
def parse_and_store_config(config_file_path):
    if not os.path.exists(config_file_path):
        print(f"Config file not found: {config_file_path}")
        return
    
    # Create a ConfigParser object to read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)
 
    with app.app_context():
        for section in config.sections():
            section_data = dict(config[section])
# Check if the section already exists in the database
            existing = ConfigData.query.filter_by(section=section).first()
            if existing:
                existing.config_json = section_data
            else:
                new_entry = ConfigData(section=section, config_json=section_data)
                db.session.add(new_entry)

        try:
            db.session.commit()
            print("Configuration saved to DB.")
        except Exception as e:
            db.session.rollback()
            print(f"DB Error: {e}")
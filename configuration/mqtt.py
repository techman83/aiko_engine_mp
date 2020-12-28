# configuration/mqtt.py: version: 2020-12-27 14:00 v05

settings = {
  "host":            "101.181.46.180",  # LCA2021 #swagbadge
# "host":            "mqtt.eclipse.org",
# "host":            "mqtt.fluux.io",
# "host":            "test.mosquitto.org",
  "keepalive":       60,
  "port":            1883,
  "topic_path":      "$me",
  "topic_subscribe": [ "$me/in", "$me/exec", upgrade_topic ],
# "topic_subscribe": [ "$me/in", "$me/exec", upgrade_topic, "$all/log" ],
  "upgrade_topic":   "upgrade/aiko_00",

# Enable processing *INSECURE* exec() commands received via MQTT
  "mqtt_insecure_exec": False
}

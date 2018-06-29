# newrelic_plugin_agent

Master: [![Build Status](https://travis-ci.org/sansible/newrelic_plugin_agent.svg?branch=master)](https://travis-ci.org/sansible/newrelic_plugin_agent)
Develop: [![Build Status](https://travis-ci.org/sansible/newrelic_plugin_agent.svg?branch=develop)](https://travis-ci.org/sansible/newrelic_plugin_agent)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This role installs the New Relic Plugin Agent. Currently configured to provide integration
with ElasticSearch and HA Proxy.



## Installation and Dependencies

To install run `ansible-galaxy install sansible.newrelic_plugin_agent` or add this to your
`roles.yml`.

```YAML
- name: sansible.newrelic_plugin_agent
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`



## Tags

This role uses tags: **build** and **configure**

* `build` - Installs ...
* `configure` - Configures ...



## Plugins

See the [Examples](#examples) section for details on how to setup these plugins.

### enabled and start_on_boot flags

Integrations should have two flags to activate them, enabled and start_on_boot.

The enabled flags covers the installation of the agent and is normally run via the
build tag; useful for baking the agent packages into an image without writing any
config or starting any services.

The start_on_boot flag will start the agent and write any required config files,
executed via the configure tag. This tag can be used for activating an agent on
a per environment basis.

### ElasticSearch

Installs the New Relic Plugin Agent with configuration for monitoring ElasticSearch.
The default settings setup the license key and write the ElasticSearch
monitoring configuration.

By default the start_on_boot flag for this agent is not enabled on boot,
in addition to allowing you to enable the service per environment you can also start
the service elsewhere once an instance has finished booting. The intention here is to
prevent flase alerts triggered by the high saturation encountered during OS boot.

### HA Proxy

Installs the New Relic Plugin Agent with configuration for monitoring HA Proxy.
The default settings setup the license key and write the HA Proxy monitoring
configuration.




## Examples

Simply include role in your playbook

Enable New Relic Plugin Agent with the ElasticSearch plugin:

```YAML
- name: Install and Configure newrelic_plugin_agent with ElasticSearch plugin
  hosts: somehost

  roles:
    - role: sansible.newrelic_plugin_agent
      sansible_newrelic_plugin_agent_enabled: yes
      sansible_newrelic_plugin_agent_license_key: 123456789123456789123456789123456789
      sansible_newrelic_plugin_agent_plugin_elasticsearch_config:
        name: my-elasticsearch-cluster
        host: es-host
        port: 9200
      sansible_newrelic_plugin_agent_plugin_elasticsearch_enabled: yes
      sansible_newrelic_plugin_agent_start_on_boot: yes
```

Enable New Relic Plugin Agent with the HA Proxy plugin:

```YAML
- name: Install and Configure newrelic_plugin_agent with HA Proxy plugin
  hosts: somehost
  
  roles:
    - role: sansible.newrelic_plugin_agent
      sansible_newrelic_plugin_agent_enabled: yes
      sansible_newrelic_plugin_agent_license_key: 12345678912345678923456789123456789
      sansible_newrelic_plugin_agent_plugin_haproxy_config:
        name: haproxy-server
        host: ha-host
        port: 80
        path: /haproxy?stats;csv
        scheme: http
      sansible_newrelic_plugin_agent_plugin_haproxy_enabled: yes
      sansible_newrelic_plugin_agent_start_on_boot: yes
```

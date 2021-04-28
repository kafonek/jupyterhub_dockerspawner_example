c.JupyterHub.authenticator_class = "jupyterhub.auth.DummyAuthenticator"
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.JupyterHub.hub_connect_ip = "jupyterhub"
c.JupyterHub.ip = "0.0.0.0"

c.DockerSpawner.image = "jupyter/minimal-notebook:latest"
c.DockerSpawner.remove = True
c.DockerSpawner.network_name = "jhub"


c.Authenticator.admin_users = set(["mvangala"])
c.Authenticator.allowed_users = set(["mvangala"])

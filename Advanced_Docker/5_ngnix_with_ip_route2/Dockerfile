# Start from the official NGINX image (Debian-based)
FROM nginx:latest

# Install iproute2 and the ping utility (iputils-ping), then clean up.
# 1. apt update: Refreshes the package list.
# 2. apt install -y ...: Installs iproute2 and the ping utility (iputils-ping).
# 3. rm -rf /var/lib/apt/lists/*: Removes the package cache to save disk space.
RUN apt update && \
    apt install -y iproute2 iputils-ping && \
    rm -rf /var/lib/apt/lists/*
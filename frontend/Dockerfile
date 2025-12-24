FROM debian:bookworm-slim

# Install lighttpd
RUN apt-get update \
    && apt-get install -y --no-install-recommends lighttpd \
    && rm -rf /var/lib/apt/lists/*

# Copy website
COPY index.html /var/www/html/index.html
COPY assets /var/www/html/assets
# Expose HTTP
EXPOSE 80

# Run lighttpd in foreground (important for containers)
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]



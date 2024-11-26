FROM odoo:11.0

USER root

# Install additional dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install any python packages
RUN pip3 install --no-cache-dir \
    num2words \
    python-dateutil \
    pytz

# Copy your custom addons
COPY ./mnt/extra-addons /mnt/extra-addons

USER odoo

# Set the correct permissions
RUN chown -R odoo:odoo /mnt/extra-addons

# Expose Odoo services
EXPOSE 8069 8071 8072

# Set the default command to run when starting the container
CMD ["odoo"]
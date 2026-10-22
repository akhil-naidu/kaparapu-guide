FROM nginx:1.27-alpine
ENV PORT=8080
COPY deploy/default.conf.template /etc/nginx/templates/default.conf.template
COPY index.html changelog.html [0-9]*.html /usr/share/nginx/html/
COPY assets /usr/share/nginx/html/assets

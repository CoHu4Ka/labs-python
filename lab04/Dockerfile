FROM jenkins/ssh-agent:alpine-jdk17

USER root
RUN apk add --no-cache php php-phar php-mbstring php-xml php-tokenizer php-json php-openssl \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

USER jenkins
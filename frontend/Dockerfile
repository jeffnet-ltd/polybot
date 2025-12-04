FROM node:18-alpine
    WORKDIR /app
    COPY package.json .
    # npm install is handled in docker-compose.yml command for quick dev iteration
    COPY . .
    # The default command is overridden by docker-compose
    CMD ["npm", "start"]

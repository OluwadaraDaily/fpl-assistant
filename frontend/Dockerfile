FROM node:20

WORKDIR /app

COPY package*.json pnpm-lock.yaml* ./

RUN npm install -g pnpm

# Prevent Cypress installation in Docker
ENV CYPRESS_INSTALL_BINARY=0

RUN pnpm install --include=dev

COPY . .

CMD ["pnpm", "dev", "--host", "0.0.0.0"]
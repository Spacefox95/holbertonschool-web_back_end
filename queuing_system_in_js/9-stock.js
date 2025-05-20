import express from "express";
import { createClient } from "redis";
import { promisify } from "util";

// DATAS
const listProducts = [
  { id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

// EXPRESS SERVER
const app = express();
const port = 1245;

// REDIS SERVER
const client = createClient();
client.on("error", (err) => console.error("Redis error:", err));
client.on("connect", () => console.log("Connected to the Redis server"));

const getAsync = promisify(client.get).bind(client);

// UTILS FUNCTIONS
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

function reserveStockById(itemId, stock) {
  return client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const value = await getAsync(`item.${itemId}`);
  const item = getItemById(itemId);
  if (!item) return 0;
  return value !== null ? parseInt(value, 10) : item.stock;
}

// ROUTES
app.get("/list_products", (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(products);
});

app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) return res.json({ status: "Product not found" });

  const currentStock = await getCurrentReservedStockById(itemId);
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentStock,
  });
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) return res.json({ status: "Product not found" });

  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock < 1)
    return res.json({ status: "Not enough stock available", itemId: itemId });

  await reserveStockById(itemId, currentStock - 1);
  return res.json({ status: "Reservation confirmed", itemId: itemId });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

package handlers

import (
	"encoding/json"
	"fmt"
	"go-http-server/models"
	"net/http"
	"sort"
	"strconv"
	"strings"
)

// Static Handlers
func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcome to the GO HTTP Server!!")
}

func AboutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "This is the about page.")
}

func ContactHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "We are available at the contact page.")
}

func APIHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintln(w, `{"message": "This is the API endpoint"}`)
}

// Temporary in-memory data
var products = []models.Product{
	{ID: 1, Name: "Laptop", Description: "A high-end computer", Price: 50000, Category: "Electronics"},
	{ID: 2, Name: "Mouse", Description: "A wireless mouse", Price: 7000, Category: "Accessories"},
	{ID: 3, Name: "Keyboard", Description: "A wireless keyboard", Price: 700, Category: "Electronics"},
}

// Fetch all products
func GetAllProducts(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(products)
}

// Fetch product by ID
func GetProductByID(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	idStr := r.URL.Query().Get("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "Invalid product ID", http.StatusBadRequest)
		return
	}
	for _, product := range products {
		if product.ID == id {
			json.NewEncoder(w).Encode(product)
			return
		}
	}
	http.Error(w, "Product not found", http.StatusNotFound)
}

// Add a new product
func AddProduct(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var newProduct models.Product
	if err := json.NewDecoder(r.Body).Decode(&newProduct); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	newProduct.ID = len(products) + 1
	products = append(products, newProduct)
	json.NewEncoder(w).Encode(newProduct)
}

// Delete a product
func DeleteProduct(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	idStr := r.URL.Query().Get("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "Invalid product ID", http.StatusBadRequest)
		return
	}
	for i, product := range products {
		if product.ID == id {
			products = append(products[:i], products[i+1:]...)
			json.NewEncoder(w).Encode(product)
			return
		}
	}
	http.Error(w, "Product not found", http.StatusNotFound)
}

// Update a product
func UpdateProduct(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	idStr := r.URL.Query().Get("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, "Invalid product ID", http.StatusBadRequest)
		return
	}
	var updatedProduct models.Product
	if err := json.NewDecoder(r.Body).Decode(&updatedProduct); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	for i, product := range products {
		if product.ID == id {
			// Retain the original ID
			updatedProduct.ID = product.ID
			products[i] = updatedProduct
			json.NewEncoder(w).Encode(products[i])
			return
		}
	}
	http.Error(w, "Product not found", http.StatusNotFound)
}

// Filter products by category
func FilterProductsByCategory(products []models.Product, category string) []models.Product {
	var result []models.Product
	for _, product := range products {
		if strings.EqualFold(product.Category, category) { // Case-insensitive match
			result = append(result, product)
		}
	}
	return result
}
func SortProductsByPrice(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	sortOrder := r.URL.Query().Get("sort")

	if sortOrder == "" {
		http.Error(w, "Missing sort order. Use 'asc' or 'desc'.", http.StatusBadRequest)
		return
	}
	// Perform sorting based on price
	sortedProducts := products // Make a copy to avoid modifying original list
	switch sortOrder {
	case "asc":
		sort.Slice(sortedProducts, func(i, j int) bool {
			return sortedProducts[i].Price < sortedProducts[j].Price
		})
	case "desc":
		sort.Slice(sortedProducts, func(i, j int) bool {
			return sortedProducts[i].Price > sortedProducts[j].Price
		})
	default:
		http.Error(w, "Invalid sort order. Use 'asc' or 'desc'.", http.StatusBadRequest)
		return
	}

	// Respond with the sorted products
	json.NewEncoder(w).Encode(sortedProducts)
}

// Filter products by name
func FilterProductsByName(products []models.Product, name string) []models.Product {
	var result []models.Product
	for _, product := range products {
		if strings.Contains(strings.ToLower(product.Name), strings.ToLower(name)) { // Substring match (case-insensitive)
			result = append(result, product)
		}
	}
	return result
}

// Get filtered products
func GetFilteredProducts(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	// Extract query parameters
	category := r.URL.Query().Get("category")
	name := r.URL.Query().Get("name")

	// Start with all products
	filteredProducts := products

	// Apply filters only if the respective parameters are provided
	if category != "" {
		filteredProducts = FilterProductsByCategory(filteredProducts, category)
	}

	if name != "" {
		filteredProducts = FilterProductsByName(filteredProducts, name)
	}

	// Handle the case where no products match the criteria
	if len(filteredProducts) == 0 {
		w.WriteHeader(http.StatusNotFound)
		json.NewEncoder(w).Encode(map[string]string{
			"error": "No products found matching the given criteria",
		})
		return
	}

	// Respond with the filtered products
	json.NewEncoder(w).Encode(filteredProducts)
}

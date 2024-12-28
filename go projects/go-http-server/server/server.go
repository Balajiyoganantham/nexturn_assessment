package server

import (
	"fmt"
	"go-http-server/handlers"
	"net/http"
)

func Start() {
	// Static Handlers
	http.HandleFunc("/", handlers.HomeHandler)
	// Request URL: http://localhost:8080/about
	http.HandleFunc("/about", handlers.AboutHandler)
	// Request URL: http://localhost:8080/contact
	http.HandleFunc("/contact", handlers.ContactHandler)
	// Request URL: http://localhost:8080/api
	http.HandleFunc("/api", handlers.APIHandler)

	// Product Handlers
	// Request URL: http://localhost:8080/products
	http.HandleFunc("/products", handlers.GetAllProducts)
	// Request URL: http://localhost:8080/products/filter
	http.HandleFunc("/products/filter", handlers.GetFilteredProducts)
	http.HandleFunc("/products/sort", handlers.SortProductsByPrice)
	// Request URL: http://localhost:8080/product
	http.HandleFunc("/product", func(w http.ResponseWriter, r *http.Request) {
		switch r.Method {
		case http.MethodGet:
			handlers.GetProductByID(w, r)
		case http.MethodPost:
			handlers.AddProduct(w, r)
		case http.MethodDelete:
			handlers.DeleteProduct(w, r)
		case http.MethodPut:
			handlers.UpdateProduct(w, r)
		default:
			http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
		}
	})

	fmt.Println("Server started on port 8080!")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Error Starting Server! ", err)
	}
}

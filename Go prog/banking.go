// Create a concurrent bank account system where multiple goroutines can deposit and
// withdraw money from a shared account. Use a mutex to prevent race conditions. Implement a
// BankAccount struct with a balance and a sync.Mutex. Create functions for Deposit(amount
// int) and Withdraw(amount int), ensuring that they are thread-safe. Start multiple goroutines
// performing deposits and withdrawals simultaneously. Print the final balance after all
// transactions.

package main

import (
	"fmt"
	"sync"
)

// BankAccount struct with balance and mutex
type BankAccount struct {
	balance int
	mu      sync.Mutex
}

// Deposit method (Thread-safe)
func (a *BankAccount) Deposit(amount int, wg *sync.WaitGroup) {
	a.mu.Lock()
	a.balance += amount
	fmt.Printf("Deposited: %d, New Balance: %d\n", amount, a.balance)
	a.mu.Unlock()
	wg.Done()
}

// Withdraw method (Thread-safe)
func (a *BankAccount) Withdraw(amount int, wg *sync.WaitGroup) {
	a.mu.Lock()
	if a.balance >= amount {
		a.balance -= amount
		fmt.Printf("Withdrew: %d, New Balance: %d\n", amount, a.balance)
	} else {
		fmt.Printf("Failed Withdrawal: %d, Insufficient Funds! Balance: %d\n", amount, a.balance)
	}
	a.mu.Unlock()
	wg.Done()
}

func main() {
	account := &BankAccount{balance: 1000} // Initial balance
	var wg sync.WaitGroup

	// Start goroutines for deposits and withdrawals
	wg.Add(6) // 6 transactions

	go account.Deposit(500, &wg)
	go account.Withdraw(300, &wg)
	go account.Withdraw(700, &wg)
	go account.Deposit(200, &wg)
	go account.Withdraw(400, &wg)
	go account.Deposit(600, &wg)

	// Wait for all transactions to complete
	wg.Wait()

	// Print final balance
	fmt.Println("Final Account Balance:", account.balance)
}

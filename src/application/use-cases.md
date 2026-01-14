# Order Use Cases

## CreateOrder
Creates a new order while enforcing all domain invariants.

## PayOrder
Marks an existing order as paid if business rules allow it.

## ShipOrder
Ships an order that has been paid and is ready for fulfillment.

## CancelOrder
Cancels an order if the current state allows cancellation.

## GetOrder
Retrieves an order by its identifier.

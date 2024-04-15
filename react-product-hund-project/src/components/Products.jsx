import { useState } from "react";
import products from "../data/seeds";
import Product from "./Product";

function Products() {
    const [productList, setProductList] = useState(products);

    const prods = products.sort((a, b) => b.votes - a.votes);
    console.log(prods);

    function handleProductUpVote(productId) {
        console.log(productId + "was upvoted.");
        const nextProducts = productList.map((product) => {
            if (product.id === productId) {
                return Object.assign({}, product, {
                    votes: product.votes + 1,
                });
            } else {
                return product;
            }
        });
        setProductList(nextProducts)
    }

    return (
        <div>
                {
                    productList.map((item, index) => (
                        <Product
                            key={index}
                            title={item.title}
                            description={item.description}
                            id={item.id}
                            imgUrl={item.productImageUrl}
                            avatarUrl={item.submitterAvatarUrl}
                            votes={item.votes}
                            onVote={handleProductUpVote} />
                    ))
                }
        </div>
    );
}

export default Products;
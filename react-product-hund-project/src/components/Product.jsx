
function Product(props) {

    function handleUpVote() {
        props.onVote(props.id)
    }

    return (
        <div className="flex mt-10  ">
            <div className="w-1/3">
                <img className="w-[150px] h-[100px]" src={props.imgUrl} />
            </div>
            
            <div className="w-2/3 flex flex-col align-middle justify-center">
                <div className="flex  " >
                    <a className="mr-3" onClick={handleUpVote}>
                    <i className="fa-solid fa-sort-up"></i>
                    </a>
                    {props.votes}
                     </div>
                <div className="description">
                    <a className="text-blue-600/100">{props.title}</a>
                    <p>{props.description}</p>
                </div>
                <div className="flex">
                    <span className="text-gray-400">Submitted by:</span>
                    <img 
                    className="rounded-full w-[35px] h-[35px]" 
                    src={props.avatarUrl} />
                </div>
            </div>
        </div>
    );
}

export default Product;
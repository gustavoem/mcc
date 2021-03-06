import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

//class Square extends React.Component {
    //render () {
        //return (
            // Both next nefinitions are equivalent.
            //<button className="square" onClick={function () {console.log ("clicked button")}}>
            //<button className="square" onClick={() => console.log ("clicked button")}>
            //<button 
                //className="square" 
                //onClick={() => this.props.onClick ()}
            //>
                //{this.props.value}
            //</button>
        //);
    //}
//}
// We can write Square as a functional component
function Square (props) {
    return (
        <button className="square" onClick={props.onClick}>
            {props.value}
        </button>
    );
}


class Board extends React.Component {
    
    renderSquare (i) {
        return (
            <Square
              value={this.props.squares[i]} 
              onClick={() => this.props.onClick (i)}
            />
        );
    }

    render () {
        return (
            <div>
            <div className="board-row">
                {this.renderSquare (0)}
                {this.renderSquare (1)}
                {this.renderSquare (2)}
            </div>
            <div className="board-row">
                {this.renderSquare (3)}
                {this.renderSquare (4)}
                {this.renderSquare (5)}
            </div>
            <div className="board-row">
                {this.renderSquare (6)}
                {this.renderSquare (7)}
                {this.renderSquare (8)}
            </div>
            </div>
        );
    }
}


//class ShoppingList extends React.Component {
    //render () {
        //return (
            //<div className="shopping-list">
            //<h1>{this.props.length }</h1>
            //<h1>Shopping List for {this.props.name}</h1>
            //<ul>
            //<li>Instagram</li>
            //<li>WhatsApp</li>
            //<li>Oculus</li>
            //</ul>
            //</div>

            // This is the code above is translated to the code bellow.
            // Most programmers use the above because of its simplicity.
            //React.createElement(
                //"div",
                //{ className: "shopping-list" },
                //React.createElement(
                    //"h1",
                    //null,
                    //"Shopping List for ",
                    //this.props.name
                //),
                //React.createElement(
                    //"ul",
                    //null,
                    //React.createElement(
                        //"li",
                        //null,
                        //"Instagram"
                        //),
                    //React.createElement(
                        //"li",
                        //null,
                        //"WhatsApp"
                        //),
                    //React.createElement(
                        //"li",
                        //null,
                        //"Oculus"
                    //)
                //)
            //)
        //);
    //}
//}


class Game extends React.Component {
    constructor (props) {
        super (props);
        this.state = {
            history: [{
                squares: Array(9).fill (null),
            }],
            xIsNext: true,
            stepNumber: 0,
        };
    }
    
    handleClick (i) {
        const history = this.state.history.slice (0, this.state.stepNumber + 1);
        const current = history[history.length - 1];
        const squares = current.squares.slice ();
        if (calculateWinner (squares) || squares[i]) {
            return;
        }
        squares[i] = (this.state.xIsNext ? 'X' : '0');
        this.setState ({
            history: history.concat ([{
                squares: squares
            }]),
            xIsNext: !this.state.xIsNext,
            stepNumber: history.length,
        });
    }

    jumpTo (step) {
        this.setState ({
            stepNumber: step,
            xIsNext: (step % 2) === 0,
        })
    }

    render () {
        const history = this.state.history;
        const current = history[this.state.stepNumber];
        const winner = calculateWinner (current.squares);
        let status;
        if (winner) {
            status = 'Winner: ' + winner;
        }
        else {
            status = 'Next player: ' + 
                (this.state.xIsNext ? 'X' : 'O');
        }

        const moves = history.map ((step, move) => {
            if (move > this.state.stepNumber)
                return null;
            const desc = move ?
                'Go to move #' + move :
                'Restart the game';
            return (
                <li key={move}>
                    <button onClick={() => this.jumpTo (move)}>
                        {desc}
                    </button>
                </li>
            );
        });

        return (
            <div className="game">
            <div className="game-board">
            <Board 
                squares={current.squares}
                onClick={(i) => this.handleClick (i)}
            />
            </div>
            <div className="game-info">
            <div>{status}</div>
            <ol>{moves}</ol>
            </div>
            </div>
        );
    }
}



// ========================================
//
 ReactDOM.render(
    <Game />,
    document.getElementById('root')
);
//


function calculateWinner(squares) {
    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
        const [a, b, c] = lines[i];
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
            return squares[a];
        }
    }
    return null;
}

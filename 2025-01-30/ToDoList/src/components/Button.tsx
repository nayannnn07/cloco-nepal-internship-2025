import { ButtonProps } from "../interfaces/ButtonProps";

function Button({ onClick, label = "" }: ButtonProps) {
    return <button onClick={onClick}>{label}</button>
}

export default Button;
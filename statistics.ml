(* Statistics Calculator in OCaml - Functional Approach *)

(* Calculate mean using List.fold_left *)
let calculate_mean lst =
  if List.length lst = 0 then 0.0
  else
    let sum = List.fold_left (fun acc x -> acc +. float_of_int x) 0.0 lst in
    sum /. float_of_int (List.length lst)

(* Calculate median using List.sort *)
let calculate_median lst =
  if List.length lst = 0 then 0.0
  else
    let sorted = List.sort compare lst in
    let len = List.length sorted in
    if len mod 2 = 0 then
      (* Even number of elements - average of two middle elements *)
      let mid1 = List.nth sorted (len / 2 - 1) in
      let mid2 = List.nth sorted (len / 2) in
      (float_of_int mid1 +. float_of_int mid2) /. 2.0
    else
      (* Odd number of elements - middle element *)
      float_of_int (List.nth sorted (len / 2))

(* Count frequency of each element using List.fold_left *)
let count_frequencies lst =
  List.fold_left
    (fun acc x ->
      if List.mem_assoc x acc then
        List.map (fun (k, v) -> if k = x then (k, v + 1) else (k, v)) acc
      else
        (x, 1) :: acc)
    [] lst

(* Find maximum frequency *)
let find_max_frequency freq_list =
  List.fold_left (fun max_freq (_, freq) -> max max_freq freq) 0 freq_list

(* Find all elements with maximum frequency *)
let find_modes lst =
  if List.length lst = 0 then []
  else
    let freq_list = count_frequencies lst in
    let max_freq = find_max_frequency freq_list in
    List.map fst (List.filter (fun (_, freq) -> freq = max_freq) freq_list)

(* Calculate mode *)
let calculate_mode lst =
  let modes = find_modes lst in
  if List.length modes = List.length (List.sort_uniq compare lst) then
    [] (* No mode if all values occur equally *)
  else
    modes

(* Helper function to print a list *)
let print_list lst =
  print_string "[";
  List.iteri (fun i x ->
    print_int x;
    if i < List.length lst - 1 then print_string ", "
  ) lst;
  print_string "]"

(* Helper function to print modes *)
let print_modes modes =
  if List.length modes = 0 then
    print_string "No mode (all values occur equally)"
  else
    print_list modes

(* Function to read integers from user input *)
let read_integers () =
  print_string "Enter a list of integers separated by spaces: ";
  flush stdout;
  
  let line = read_line () in
  let words = String.split_on_char ' ' line in
  
  let rec parse_integers words acc =
    match words with
    | [] -> List.rev acc
    | word :: rest ->
        try
          let num = int_of_string (String.trim word) in
          parse_integers rest (num :: acc)
        with Failure _ ->
          (* Skip invalid integers *)
          parse_integers rest acc
  in
  
  parse_integers words []

(* Main function *)
let main () =
  print_endline "=== Statistics Calculator (OCaml - Functional) ===";
  print_newline ();
  
  (* Read data from user input *)
  let data = read_integers () in
  
  if List.length data = 0 then (
    print_endline "No valid integers entered.";
    exit 1
  );
  
  print_string "Input data: ";
  print_list data;
  print_newline ();
  print_newline ();
  
  (* Calculate and display statistics *)
  let mean = calculate_mean data in
  Printf.printf "Mean: %.2f\n" mean;
  
  let median = calculate_median data in
  Printf.printf "Median: %.2f\n" median;
  
  let modes = calculate_mode data in
  print_string "Mode: ";
  print_modes modes;
  print_newline ()

(* Run the main function *)
let () = main () 
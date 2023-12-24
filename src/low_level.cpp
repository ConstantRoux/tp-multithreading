#include <cpr/cpr.h>

#include <Eigen/Dense>
#include <chrono>
#include <iostream>
#include <nlohmann/json.hpp>

#define CODE_SUCCESS 200
#define NB_CORES 4

class Minion {
 private:
  int identifier;
  int size;

  Eigen::MatrixXd A;
  Eigen::VectorXd X;
  Eigen::VectorXd b;

  double execution_time;

 public:
  Minion() {
    while (!initialization())
      ;
    work();
  }

  bool initialization() {
    cpr::Response response = cpr::Get(cpr::Url{"http://localhost:8000"});
    if (response.status_code != CODE_SUCCESS) {
      return false;
    }

    nlohmann::json data_json = nlohmann::json::parse(response.text);
    identifier = data_json["identifier"];
    size = data_json["size"];

    A.resize(size, size);
    b.resize(size);

    for (unsigned long i = 0; i < size; i++) {
      for (unsigned long j = 0; j < size; j++) {
        A(i, j) = data_json["A"][i][j];
      }
      b(i) = data_json["b"][i];
    }

    std::cout << "Minion for task " << identifier << " initialized"
              << std::endl;

    return true;
  }

  double work() {
    /**
    Performs the task by solving a linear system AX=B.

    Uses the generated random vectors A and b of the specified size, solves the
    linear system AX=b using numpy.linalg.solve, saves the solution in X,
    measures the execution time, and prints in DEBUG the solution.

    :return: The execution time of the task in seconds.
    */
    // solve linear system ax=b and measure start and stop time
    const auto start_time = std::chrono::high_resolution_clock::now();
    X = A.lu().solve(b);
    const auto end_time = std::chrono::high_resolution_clock::now();

    // compute execution time
    execution_time = std::chrono::duration_cast<std::chrono::duration<double>>(
                         end_time - start_time)
                         .count();

    // print the task id and the execution time
    std::cout << "Task " << identifier << ": " << execution_time << " seconds"
              << std::endl;

    // return execution time
    return execution_time;
  }
};

int main() {
  // Eigen::setNbThreads(NB_CORES);
  Minion minion;

  exit(0);
}

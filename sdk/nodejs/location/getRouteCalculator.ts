// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Definition of AWS::Location::RouteCalculator Resource Type
 */
export function getRouteCalculator(args: GetRouteCalculatorArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteCalculatorResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:location:getRouteCalculator", {
        "calculatorName": args.calculatorName,
    }, opts);
}

export interface GetRouteCalculatorArgs {
    calculatorName: string;
}

export interface GetRouteCalculatorResult {
    readonly arn?: string;
    readonly calculatorArn?: string;
    readonly createTime?: string;
    readonly updateTime?: string;
}
/**
 * Definition of AWS::Location::RouteCalculator Resource Type
 */
export function getRouteCalculatorOutput(args: GetRouteCalculatorOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRouteCalculatorResult> {
    return pulumi.output(args).apply((a: any) => getRouteCalculator(a, opts))
}

export interface GetRouteCalculatorOutputArgs {
    calculatorName: pulumi.Input<string>;
}

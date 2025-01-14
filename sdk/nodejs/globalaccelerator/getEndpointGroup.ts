// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::GlobalAccelerator::EndpointGroup
 */
export function getEndpointGroup(args: GetEndpointGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetEndpointGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:globalaccelerator:getEndpointGroup", {
        "endpointGroupArn": args.endpointGroupArn,
    }, opts);
}

export interface GetEndpointGroupArgs {
    /**
     * The Amazon Resource Name (ARN) of the endpoint group
     */
    endpointGroupArn: string;
}

export interface GetEndpointGroupResult {
    /**
     * The list of endpoint objects.
     */
    readonly endpointConfigurations?: outputs.globalaccelerator.EndpointGroupEndpointConfiguration[];
    /**
     * The Amazon Resource Name (ARN) of the endpoint group
     */
    readonly endpointGroupArn?: string;
    /**
     * The time in seconds between each health check for an endpoint. Must be a value of 10 or 30
     */
    readonly healthCheckIntervalSeconds?: number;
    readonly healthCheckPath?: string;
    /**
     * The port that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
     */
    readonly healthCheckPort?: number;
    /**
     * The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
     */
    readonly healthCheckProtocol?: enums.globalaccelerator.EndpointGroupHealthCheckProtocol;
    readonly portOverrides?: outputs.globalaccelerator.EndpointGroupPortOverride[];
    /**
     * The number of consecutive health checks required to set the state of the endpoint to unhealthy.
     */
    readonly thresholdCount?: number;
    /**
     * The percentage of traffic to sent to an AWS Region
     */
    readonly trafficDialPercentage?: number;
}
/**
 * Resource Type definition for AWS::GlobalAccelerator::EndpointGroup
 */
export function getEndpointGroupOutput(args: GetEndpointGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEndpointGroupResult> {
    return pulumi.output(args).apply((a: any) => getEndpointGroup(a, opts))
}

export interface GetEndpointGroupOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the endpoint group
     */
    endpointGroupArn: pulumi.Input<string>;
}

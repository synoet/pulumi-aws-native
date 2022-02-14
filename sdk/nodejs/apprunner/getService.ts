// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::AppRunner::Service resource specifies an AppRunner Service.
 */
export function getService(args: GetServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:apprunner:getService", {
        "serviceArn": args.serviceArn,
    }, opts);
}

export interface GetServiceArgs {
    /**
     * The Amazon Resource Name (ARN) of the AppRunner Service.
     */
    serviceArn: string;
}

export interface GetServiceResult {
    readonly healthCheckConfiguration?: outputs.apprunner.ServiceHealthCheckConfiguration;
    readonly instanceConfiguration?: outputs.apprunner.ServiceInstanceConfiguration;
    readonly networkConfiguration?: outputs.apprunner.ServiceNetworkConfiguration;
    /**
     * The Amazon Resource Name (ARN) of the AppRunner Service.
     */
    readonly serviceArn?: string;
    /**
     * The AppRunner Service Id
     */
    readonly serviceId?: string;
    /**
     * The Service Url of the AppRunner Service.
     */
    readonly serviceUrl?: string;
    readonly sourceConfiguration?: outputs.apprunner.ServiceSourceConfiguration;
    /**
     * AppRunner Service status.
     */
    readonly status?: string;
}

export function getServiceOutput(args: GetServiceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceResult> {
    return pulumi.output(args).apply(a => getService(a, opts))
}

export interface GetServiceOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the AppRunner Service.
     */
    serviceArn: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IAM::ServiceLinkedRole
 */
export function getServiceLinkedRole(args: GetServiceLinkedRoleArgs, opts?: pulumi.InvokeOptions): Promise<GetServiceLinkedRoleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iam:getServiceLinkedRole", {
        "id": args.id,
    }, opts);
}

export interface GetServiceLinkedRoleArgs {
    id: string;
}

export interface GetServiceLinkedRoleResult {
    readonly description?: string;
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::IAM::ServiceLinkedRole
 */
export function getServiceLinkedRoleOutput(args: GetServiceLinkedRoleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetServiceLinkedRoleResult> {
    return pulumi.output(args).apply((a: any) => getServiceLinkedRole(a, opts))
}

export interface GetServiceLinkedRoleOutputArgs {
    id: pulumi.Input<string>;
}

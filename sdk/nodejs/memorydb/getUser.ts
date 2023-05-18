// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::MemoryDB::User
 */
export function getUser(args: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:memorydb:getUser", {
        "userName": args.userName,
    }, opts);
}

export interface GetUserArgs {
    /**
     * The name of the user.
     */
    userName: string;
}

export interface GetUserResult {
    /**
     * The Amazon Resource Name (ARN) of the user account.
     */
    readonly arn?: string;
    /**
     * Indicates the user status. Can be "active", "modifying" or "deleting".
     */
    readonly status?: string;
    /**
     * An array of key-value pairs to apply to this user.
     */
    readonly tags?: outputs.memorydb.UserTag[];
}
/**
 * Resource Type definition for AWS::MemoryDB::User
 */
export function getUserOutput(args: GetUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserResult> {
    return pulumi.output(args).apply((a: any) => getUser(a, opts))
}

export interface GetUserOutputArgs {
    /**
     * The name of the user.
     */
    userName: pulumi.Input<string>;
}

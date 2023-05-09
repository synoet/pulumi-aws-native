// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation
 */
export function getResourceAssociation(args: GetResourceAssociationArgs, opts?: pulumi.InvokeOptions): Promise<GetResourceAssociationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:servicecatalogappregistry:getResourceAssociation", {
        "id": args.id,
    }, opts);
}

export interface GetResourceAssociationArgs {
    id: string;
}

export interface GetResourceAssociationResult {
    readonly applicationArn?: string;
    readonly id?: string;
    readonly resourceArn?: string;
}
/**
 * Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation
 */
export function getResourceAssociationOutput(args: GetResourceAssociationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetResourceAssociationResult> {
    return pulumi.output(args).apply((a: any) => getResourceAssociation(a, opts))
}

export interface GetResourceAssociationOutputArgs {
    id: pulumi.Input<string>;
}

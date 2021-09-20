// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html
 */
export class ReplicationConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing ReplicationConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ReplicationConfiguration {
        return new ReplicationConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ecr:ReplicationConfiguration';

    /**
     * Returns true if the given object is an instance of ReplicationConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReplicationConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReplicationConfiguration.__pulumiType;
    }

    /**
     * The RegistryId associated with the aws account.
     */
    public /*out*/ readonly registryId!: pulumi.Output<string>;
    public readonly replicationConfiguration!: pulumi.Output<outputs.ecr.ReplicationConfigurationReplicationConfiguration>;

    /**
     * Create a ReplicationConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ReplicationConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.replicationConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'replicationConfiguration'");
            }
            inputs["replicationConfiguration"] = args ? args.replicationConfiguration : undefined;
            inputs["registryId"] = undefined /*out*/;
        } else {
            inputs["registryId"] = undefined /*out*/;
            inputs["replicationConfiguration"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ReplicationConfiguration.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ReplicationConfiguration resource.
 */
export interface ReplicationConfigurationArgs {
    replicationConfiguration: pulumi.Input<inputs.ecr.ReplicationConfigurationReplicationConfigurationArgs>;
}

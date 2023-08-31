// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Associate a set of ECS Capacity Providers with a specified ECS Cluster
 */
export class ClusterCapacityProviderAssociations extends pulumi.CustomResource {
    /**
     * Get an existing ClusterCapacityProviderAssociations resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ClusterCapacityProviderAssociations {
        return new ClusterCapacityProviderAssociations(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ecs:ClusterCapacityProviderAssociations';

    /**
     * Returns true if the given object is an instance of ClusterCapacityProviderAssociations.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ClusterCapacityProviderAssociations {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ClusterCapacityProviderAssociations.__pulumiType;
    }

    public readonly capacityProviders!: pulumi.Output<(enums.ecs.ClusterCapacityProviderAssociationsCapacityProvider | string)[]>;
    public readonly cluster!: pulumi.Output<string>;
    public readonly defaultCapacityProviderStrategy!: pulumi.Output<outputs.ecs.ClusterCapacityProviderAssociationsCapacityProviderStrategy[]>;

    /**
     * Create a ClusterCapacityProviderAssociations resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterCapacityProviderAssociationsArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.capacityProviders === undefined) && !opts.urn) {
                throw new Error("Missing required property 'capacityProviders'");
            }
            if ((!args || args.cluster === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cluster'");
            }
            if ((!args || args.defaultCapacityProviderStrategy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'defaultCapacityProviderStrategy'");
            }
            resourceInputs["capacityProviders"] = args ? args.capacityProviders : undefined;
            resourceInputs["cluster"] = args ? args.cluster : undefined;
            resourceInputs["defaultCapacityProviderStrategy"] = args ? args.defaultCapacityProviderStrategy : undefined;
        } else {
            resourceInputs["capacityProviders"] = undefined /*out*/;
            resourceInputs["cluster"] = undefined /*out*/;
            resourceInputs["defaultCapacityProviderStrategy"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["cluster"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ClusterCapacityProviderAssociations.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ClusterCapacityProviderAssociations resource.
 */
export interface ClusterCapacityProviderAssociationsArgs {
    capacityProviders: pulumi.Input<pulumi.Input<enums.ecs.ClusterCapacityProviderAssociationsCapacityProvider | string>[]>;
    cluster: pulumi.Input<string>;
    defaultCapacityProviderStrategy: pulumi.Input<pulumi.Input<inputs.ecs.ClusterCapacityProviderAssociationsCapacityProviderStrategyArgs>[]>;
}

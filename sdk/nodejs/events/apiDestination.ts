// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Events::ApiDestination.
 */
export class ApiDestination extends pulumi.CustomResource {
    /**
     * Get an existing ApiDestination resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ApiDestination {
        return new ApiDestination(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:events:ApiDestination';

    /**
     * Returns true if the given object is an instance of ApiDestination.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiDestination {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiDestination.__pulumiType;
    }

    /**
     * The arn of the api destination.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The arn of the connection.
     */
    public readonly connectionArn!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly httpMethod!: pulumi.Output<enums.events.ApiDestinationHttpMethod>;
    /**
     * Url endpoint to invoke.
     */
    public readonly invocationEndpoint!: pulumi.Output<string>;
    public readonly invocationRateLimitPerSecond!: pulumi.Output<number | undefined>;
    /**
     * Name of the apiDestination.
     */
    public readonly name!: pulumi.Output<string | undefined>;

    /**
     * Create a ApiDestination resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApiDestinationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.connectionArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connectionArn'");
            }
            if ((!args || args.httpMethod === undefined) && !opts.urn) {
                throw new Error("Missing required property 'httpMethod'");
            }
            if ((!args || args.invocationEndpoint === undefined) && !opts.urn) {
                throw new Error("Missing required property 'invocationEndpoint'");
            }
            resourceInputs["connectionArn"] = args ? args.connectionArn : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["httpMethod"] = args ? args.httpMethod : undefined;
            resourceInputs["invocationEndpoint"] = args ? args.invocationEndpoint : undefined;
            resourceInputs["invocationRateLimitPerSecond"] = args ? args.invocationRateLimitPerSecond : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["connectionArn"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["httpMethod"] = undefined /*out*/;
            resourceInputs["invocationEndpoint"] = undefined /*out*/;
            resourceInputs["invocationRateLimitPerSecond"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ApiDestination.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ApiDestination resource.
 */
export interface ApiDestinationArgs {
    /**
     * The arn of the connection.
     */
    connectionArn: pulumi.Input<string>;
    description?: pulumi.Input<string>;
    httpMethod: pulumi.Input<enums.events.ApiDestinationHttpMethod>;
    /**
     * Url endpoint to invoke.
     */
    invocationEndpoint: pulumi.Input<string>;
    invocationRateLimitPerSecond?: pulumi.Input<number>;
    /**
     * Name of the apiDestination.
     */
    name?: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ApiGatewayV2::ApiGatewayManagedOverrides
 *
 * @deprecated ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ApiGatewayManagedOverrides extends pulumi.CustomResource {
    /**
     * Get an existing ApiGatewayManagedOverrides resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ApiGatewayManagedOverrides {
        pulumi.log.warn("ApiGatewayManagedOverrides is deprecated: ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ApiGatewayManagedOverrides(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apigatewayv2:ApiGatewayManagedOverrides';

    /**
     * Returns true if the given object is an instance of ApiGatewayManagedOverrides.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiGatewayManagedOverrides {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiGatewayManagedOverrides.__pulumiType;
    }

    public readonly apiId!: pulumi.Output<string>;
    public readonly integration!: pulumi.Output<outputs.apigatewayv2.ApiGatewayManagedOverridesIntegrationOverrides | undefined>;
    public readonly route!: pulumi.Output<outputs.apigatewayv2.ApiGatewayManagedOverridesRouteOverrides | undefined>;
    public readonly stage!: pulumi.Output<outputs.apigatewayv2.ApiGatewayManagedOverridesStageOverrides | undefined>;

    /**
     * Create a ApiGatewayManagedOverrides resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ApiGatewayManagedOverridesArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ApiGatewayManagedOverrides is deprecated: ApiGatewayManagedOverrides is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            resourceInputs["apiId"] = args ? args.apiId : undefined;
            resourceInputs["integration"] = args ? args.integration : undefined;
            resourceInputs["route"] = args ? args.route : undefined;
            resourceInputs["stage"] = args ? args.stage : undefined;
        } else {
            resourceInputs["apiId"] = undefined /*out*/;
            resourceInputs["integration"] = undefined /*out*/;
            resourceInputs["route"] = undefined /*out*/;
            resourceInputs["stage"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["apiId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ApiGatewayManagedOverrides.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ApiGatewayManagedOverrides resource.
 */
export interface ApiGatewayManagedOverridesArgs {
    apiId: pulumi.Input<string>;
    integration?: pulumi.Input<inputs.apigatewayv2.ApiGatewayManagedOverridesIntegrationOverridesArgs>;
    route?: pulumi.Input<inputs.apigatewayv2.ApiGatewayManagedOverridesRouteOverridesArgs>;
    stage?: pulumi.Input<inputs.apigatewayv2.ApiGatewayManagedOverridesStageOverridesArgs>;
}

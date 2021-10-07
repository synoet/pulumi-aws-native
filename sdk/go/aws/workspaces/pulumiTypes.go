// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package workspaces

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type ConnectionAliasAssociation struct {
	AssociatedAccountId  *string                                      `pulumi:"associatedAccountId"`
	AssociationStatus    *ConnectionAliasAssociationAssociationStatus `pulumi:"associationStatus"`
	ConnectionIdentifier *string                                      `pulumi:"connectionIdentifier"`
	ResourceId           *string                                      `pulumi:"resourceId"`
}

// ConnectionAliasAssociationInput is an input type that accepts ConnectionAliasAssociationArgs and ConnectionAliasAssociationOutput values.
// You can construct a concrete instance of `ConnectionAliasAssociationInput` via:
//
//          ConnectionAliasAssociationArgs{...}
type ConnectionAliasAssociationInput interface {
	pulumi.Input

	ToConnectionAliasAssociationOutput() ConnectionAliasAssociationOutput
	ToConnectionAliasAssociationOutputWithContext(context.Context) ConnectionAliasAssociationOutput
}

type ConnectionAliasAssociationArgs struct {
	AssociatedAccountId  pulumi.StringPtrInput                               `pulumi:"associatedAccountId"`
	AssociationStatus    ConnectionAliasAssociationAssociationStatusPtrInput `pulumi:"associationStatus"`
	ConnectionIdentifier pulumi.StringPtrInput                               `pulumi:"connectionIdentifier"`
	ResourceId           pulumi.StringPtrInput                               `pulumi:"resourceId"`
}

func (ConnectionAliasAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasAssociation)(nil)).Elem()
}

func (i ConnectionAliasAssociationArgs) ToConnectionAliasAssociationOutput() ConnectionAliasAssociationOutput {
	return i.ToConnectionAliasAssociationOutputWithContext(context.Background())
}

func (i ConnectionAliasAssociationArgs) ToConnectionAliasAssociationOutputWithContext(ctx context.Context) ConnectionAliasAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasAssociationOutput)
}

// ConnectionAliasAssociationArrayInput is an input type that accepts ConnectionAliasAssociationArray and ConnectionAliasAssociationArrayOutput values.
// You can construct a concrete instance of `ConnectionAliasAssociationArrayInput` via:
//
//          ConnectionAliasAssociationArray{ ConnectionAliasAssociationArgs{...} }
type ConnectionAliasAssociationArrayInput interface {
	pulumi.Input

	ToConnectionAliasAssociationArrayOutput() ConnectionAliasAssociationArrayOutput
	ToConnectionAliasAssociationArrayOutputWithContext(context.Context) ConnectionAliasAssociationArrayOutput
}

type ConnectionAliasAssociationArray []ConnectionAliasAssociationInput

func (ConnectionAliasAssociationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasAssociation)(nil)).Elem()
}

func (i ConnectionAliasAssociationArray) ToConnectionAliasAssociationArrayOutput() ConnectionAliasAssociationArrayOutput {
	return i.ToConnectionAliasAssociationArrayOutputWithContext(context.Background())
}

func (i ConnectionAliasAssociationArray) ToConnectionAliasAssociationArrayOutputWithContext(ctx context.Context) ConnectionAliasAssociationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasAssociationArrayOutput)
}

type ConnectionAliasAssociationOutput struct{ *pulumi.OutputState }

func (ConnectionAliasAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasAssociation)(nil)).Elem()
}

func (o ConnectionAliasAssociationOutput) ToConnectionAliasAssociationOutput() ConnectionAliasAssociationOutput {
	return o
}

func (o ConnectionAliasAssociationOutput) ToConnectionAliasAssociationOutputWithContext(ctx context.Context) ConnectionAliasAssociationOutput {
	return o
}

func (o ConnectionAliasAssociationOutput) AssociatedAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ConnectionAliasAssociation) *string { return v.AssociatedAccountId }).(pulumi.StringPtrOutput)
}

func (o ConnectionAliasAssociationOutput) AssociationStatus() ConnectionAliasAssociationAssociationStatusPtrOutput {
	return o.ApplyT(func(v ConnectionAliasAssociation) *ConnectionAliasAssociationAssociationStatus {
		return v.AssociationStatus
	}).(ConnectionAliasAssociationAssociationStatusPtrOutput)
}

func (o ConnectionAliasAssociationOutput) ConnectionIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ConnectionAliasAssociation) *string { return v.ConnectionIdentifier }).(pulumi.StringPtrOutput)
}

func (o ConnectionAliasAssociationOutput) ResourceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ConnectionAliasAssociation) *string { return v.ResourceId }).(pulumi.StringPtrOutput)
}

type ConnectionAliasAssociationArrayOutput struct{ *pulumi.OutputState }

func (ConnectionAliasAssociationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasAssociation)(nil)).Elem()
}

func (o ConnectionAliasAssociationArrayOutput) ToConnectionAliasAssociationArrayOutput() ConnectionAliasAssociationArrayOutput {
	return o
}

func (o ConnectionAliasAssociationArrayOutput) ToConnectionAliasAssociationArrayOutputWithContext(ctx context.Context) ConnectionAliasAssociationArrayOutput {
	return o
}

func (o ConnectionAliasAssociationArrayOutput) Index(i pulumi.IntInput) ConnectionAliasAssociationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ConnectionAliasAssociation {
		return vs[0].([]ConnectionAliasAssociation)[vs[1].(int)]
	}).(ConnectionAliasAssociationOutput)
}

type ConnectionAliasTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// ConnectionAliasTagInput is an input type that accepts ConnectionAliasTagArgs and ConnectionAliasTagOutput values.
// You can construct a concrete instance of `ConnectionAliasTagInput` via:
//
//          ConnectionAliasTagArgs{...}
type ConnectionAliasTagInput interface {
	pulumi.Input

	ToConnectionAliasTagOutput() ConnectionAliasTagOutput
	ToConnectionAliasTagOutputWithContext(context.Context) ConnectionAliasTagOutput
}

type ConnectionAliasTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (ConnectionAliasTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasTag)(nil)).Elem()
}

func (i ConnectionAliasTagArgs) ToConnectionAliasTagOutput() ConnectionAliasTagOutput {
	return i.ToConnectionAliasTagOutputWithContext(context.Background())
}

func (i ConnectionAliasTagArgs) ToConnectionAliasTagOutputWithContext(ctx context.Context) ConnectionAliasTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasTagOutput)
}

// ConnectionAliasTagArrayInput is an input type that accepts ConnectionAliasTagArray and ConnectionAliasTagArrayOutput values.
// You can construct a concrete instance of `ConnectionAliasTagArrayInput` via:
//
//          ConnectionAliasTagArray{ ConnectionAliasTagArgs{...} }
type ConnectionAliasTagArrayInput interface {
	pulumi.Input

	ToConnectionAliasTagArrayOutput() ConnectionAliasTagArrayOutput
	ToConnectionAliasTagArrayOutputWithContext(context.Context) ConnectionAliasTagArrayOutput
}

type ConnectionAliasTagArray []ConnectionAliasTagInput

func (ConnectionAliasTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasTag)(nil)).Elem()
}

func (i ConnectionAliasTagArray) ToConnectionAliasTagArrayOutput() ConnectionAliasTagArrayOutput {
	return i.ToConnectionAliasTagArrayOutputWithContext(context.Background())
}

func (i ConnectionAliasTagArray) ToConnectionAliasTagArrayOutputWithContext(ctx context.Context) ConnectionAliasTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectionAliasTagArrayOutput)
}

type ConnectionAliasTagOutput struct{ *pulumi.OutputState }

func (ConnectionAliasTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ConnectionAliasTag)(nil)).Elem()
}

func (o ConnectionAliasTagOutput) ToConnectionAliasTagOutput() ConnectionAliasTagOutput {
	return o
}

func (o ConnectionAliasTagOutput) ToConnectionAliasTagOutputWithContext(ctx context.Context) ConnectionAliasTagOutput {
	return o
}

func (o ConnectionAliasTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionAliasTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o ConnectionAliasTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v ConnectionAliasTag) string { return v.Value }).(pulumi.StringOutput)
}

type ConnectionAliasTagArrayOutput struct{ *pulumi.OutputState }

func (ConnectionAliasTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]ConnectionAliasTag)(nil)).Elem()
}

func (o ConnectionAliasTagArrayOutput) ToConnectionAliasTagArrayOutput() ConnectionAliasTagArrayOutput {
	return o
}

func (o ConnectionAliasTagArrayOutput) ToConnectionAliasTagArrayOutputWithContext(ctx context.Context) ConnectionAliasTagArrayOutput {
	return o
}

func (o ConnectionAliasTagArrayOutput) Index(i pulumi.IntInput) ConnectionAliasTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) ConnectionAliasTag {
		return vs[0].([]ConnectionAliasTag)[vs[1].(int)]
	}).(ConnectionAliasTagOutput)
}

type WorkspaceProperties struct {
	ComputeTypeName                     *string `pulumi:"computeTypeName"`
	RootVolumeSizeGib                   *int    `pulumi:"rootVolumeSizeGib"`
	RunningMode                         *string `pulumi:"runningMode"`
	RunningModeAutoStopTimeoutInMinutes *int    `pulumi:"runningModeAutoStopTimeoutInMinutes"`
	UserVolumeSizeGib                   *int    `pulumi:"userVolumeSizeGib"`
}

// WorkspacePropertiesInput is an input type that accepts WorkspacePropertiesArgs and WorkspacePropertiesOutput values.
// You can construct a concrete instance of `WorkspacePropertiesInput` via:
//
//          WorkspacePropertiesArgs{...}
type WorkspacePropertiesInput interface {
	pulumi.Input

	ToWorkspacePropertiesOutput() WorkspacePropertiesOutput
	ToWorkspacePropertiesOutputWithContext(context.Context) WorkspacePropertiesOutput
}

type WorkspacePropertiesArgs struct {
	ComputeTypeName                     pulumi.StringPtrInput `pulumi:"computeTypeName"`
	RootVolumeSizeGib                   pulumi.IntPtrInput    `pulumi:"rootVolumeSizeGib"`
	RunningMode                         pulumi.StringPtrInput `pulumi:"runningMode"`
	RunningModeAutoStopTimeoutInMinutes pulumi.IntPtrInput    `pulumi:"runningModeAutoStopTimeoutInMinutes"`
	UserVolumeSizeGib                   pulumi.IntPtrInput    `pulumi:"userVolumeSizeGib"`
}

func (WorkspacePropertiesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkspaceProperties)(nil)).Elem()
}

func (i WorkspacePropertiesArgs) ToWorkspacePropertiesOutput() WorkspacePropertiesOutput {
	return i.ToWorkspacePropertiesOutputWithContext(context.Background())
}

func (i WorkspacePropertiesArgs) ToWorkspacePropertiesOutputWithContext(ctx context.Context) WorkspacePropertiesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspacePropertiesOutput)
}

func (i WorkspacePropertiesArgs) ToWorkspacePropertiesPtrOutput() WorkspacePropertiesPtrOutput {
	return i.ToWorkspacePropertiesPtrOutputWithContext(context.Background())
}

func (i WorkspacePropertiesArgs) ToWorkspacePropertiesPtrOutputWithContext(ctx context.Context) WorkspacePropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspacePropertiesOutput).ToWorkspacePropertiesPtrOutputWithContext(ctx)
}

// WorkspacePropertiesPtrInput is an input type that accepts WorkspacePropertiesArgs, WorkspacePropertiesPtr and WorkspacePropertiesPtrOutput values.
// You can construct a concrete instance of `WorkspacePropertiesPtrInput` via:
//
//          WorkspacePropertiesArgs{...}
//
//  or:
//
//          nil
type WorkspacePropertiesPtrInput interface {
	pulumi.Input

	ToWorkspacePropertiesPtrOutput() WorkspacePropertiesPtrOutput
	ToWorkspacePropertiesPtrOutputWithContext(context.Context) WorkspacePropertiesPtrOutput
}

type workspacePropertiesPtrType WorkspacePropertiesArgs

func WorkspacePropertiesPtr(v *WorkspacePropertiesArgs) WorkspacePropertiesPtrInput {
	return (*workspacePropertiesPtrType)(v)
}

func (*workspacePropertiesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkspaceProperties)(nil)).Elem()
}

func (i *workspacePropertiesPtrType) ToWorkspacePropertiesPtrOutput() WorkspacePropertiesPtrOutput {
	return i.ToWorkspacePropertiesPtrOutputWithContext(context.Background())
}

func (i *workspacePropertiesPtrType) ToWorkspacePropertiesPtrOutputWithContext(ctx context.Context) WorkspacePropertiesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspacePropertiesPtrOutput)
}

type WorkspacePropertiesOutput struct{ *pulumi.OutputState }

func (WorkspacePropertiesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkspaceProperties)(nil)).Elem()
}

func (o WorkspacePropertiesOutput) ToWorkspacePropertiesOutput() WorkspacePropertiesOutput {
	return o
}

func (o WorkspacePropertiesOutput) ToWorkspacePropertiesOutputWithContext(ctx context.Context) WorkspacePropertiesOutput {
	return o
}

func (o WorkspacePropertiesOutput) ToWorkspacePropertiesPtrOutput() WorkspacePropertiesPtrOutput {
	return o.ToWorkspacePropertiesPtrOutputWithContext(context.Background())
}

func (o WorkspacePropertiesOutput) ToWorkspacePropertiesPtrOutputWithContext(ctx context.Context) WorkspacePropertiesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v WorkspaceProperties) *WorkspaceProperties {
		return &v
	}).(WorkspacePropertiesPtrOutput)
}

func (o WorkspacePropertiesOutput) ComputeTypeName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkspaceProperties) *string { return v.ComputeTypeName }).(pulumi.StringPtrOutput)
}

func (o WorkspacePropertiesOutput) RootVolumeSizeGib() pulumi.IntPtrOutput {
	return o.ApplyT(func(v WorkspaceProperties) *int { return v.RootVolumeSizeGib }).(pulumi.IntPtrOutput)
}

func (o WorkspacePropertiesOutput) RunningMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v WorkspaceProperties) *string { return v.RunningMode }).(pulumi.StringPtrOutput)
}

func (o WorkspacePropertiesOutput) RunningModeAutoStopTimeoutInMinutes() pulumi.IntPtrOutput {
	return o.ApplyT(func(v WorkspaceProperties) *int { return v.RunningModeAutoStopTimeoutInMinutes }).(pulumi.IntPtrOutput)
}

func (o WorkspacePropertiesOutput) UserVolumeSizeGib() pulumi.IntPtrOutput {
	return o.ApplyT(func(v WorkspaceProperties) *int { return v.UserVolumeSizeGib }).(pulumi.IntPtrOutput)
}

type WorkspacePropertiesPtrOutput struct{ *pulumi.OutputState }

func (WorkspacePropertiesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkspaceProperties)(nil)).Elem()
}

func (o WorkspacePropertiesPtrOutput) ToWorkspacePropertiesPtrOutput() WorkspacePropertiesPtrOutput {
	return o
}

func (o WorkspacePropertiesPtrOutput) ToWorkspacePropertiesPtrOutputWithContext(ctx context.Context) WorkspacePropertiesPtrOutput {
	return o
}

func (o WorkspacePropertiesPtrOutput) Elem() WorkspacePropertiesOutput {
	return o.ApplyT(func(v *WorkspaceProperties) WorkspaceProperties {
		if v != nil {
			return *v
		}
		var ret WorkspaceProperties
		return ret
	}).(WorkspacePropertiesOutput)
}

func (o WorkspacePropertiesPtrOutput) ComputeTypeName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WorkspaceProperties) *string {
		if v == nil {
			return nil
		}
		return v.ComputeTypeName
	}).(pulumi.StringPtrOutput)
}

func (o WorkspacePropertiesPtrOutput) RootVolumeSizeGib() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *WorkspaceProperties) *int {
		if v == nil {
			return nil
		}
		return v.RootVolumeSizeGib
	}).(pulumi.IntPtrOutput)
}

func (o WorkspacePropertiesPtrOutput) RunningMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *WorkspaceProperties) *string {
		if v == nil {
			return nil
		}
		return v.RunningMode
	}).(pulumi.StringPtrOutput)
}

func (o WorkspacePropertiesPtrOutput) RunningModeAutoStopTimeoutInMinutes() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *WorkspaceProperties) *int {
		if v == nil {
			return nil
		}
		return v.RunningModeAutoStopTimeoutInMinutes
	}).(pulumi.IntPtrOutput)
}

func (o WorkspacePropertiesPtrOutput) UserVolumeSizeGib() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *WorkspaceProperties) *int {
		if v == nil {
			return nil
		}
		return v.UserVolumeSizeGib
	}).(pulumi.IntPtrOutput)
}

type WorkspaceTag struct {
	Key   string `pulumi:"key"`
	Value string `pulumi:"value"`
}

// WorkspaceTagInput is an input type that accepts WorkspaceTagArgs and WorkspaceTagOutput values.
// You can construct a concrete instance of `WorkspaceTagInput` via:
//
//          WorkspaceTagArgs{...}
type WorkspaceTagInput interface {
	pulumi.Input

	ToWorkspaceTagOutput() WorkspaceTagOutput
	ToWorkspaceTagOutputWithContext(context.Context) WorkspaceTagOutput
}

type WorkspaceTagArgs struct {
	Key   pulumi.StringInput `pulumi:"key"`
	Value pulumi.StringInput `pulumi:"value"`
}

func (WorkspaceTagArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkspaceTag)(nil)).Elem()
}

func (i WorkspaceTagArgs) ToWorkspaceTagOutput() WorkspaceTagOutput {
	return i.ToWorkspaceTagOutputWithContext(context.Background())
}

func (i WorkspaceTagArgs) ToWorkspaceTagOutputWithContext(ctx context.Context) WorkspaceTagOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceTagOutput)
}

// WorkspaceTagArrayInput is an input type that accepts WorkspaceTagArray and WorkspaceTagArrayOutput values.
// You can construct a concrete instance of `WorkspaceTagArrayInput` via:
//
//          WorkspaceTagArray{ WorkspaceTagArgs{...} }
type WorkspaceTagArrayInput interface {
	pulumi.Input

	ToWorkspaceTagArrayOutput() WorkspaceTagArrayOutput
	ToWorkspaceTagArrayOutputWithContext(context.Context) WorkspaceTagArrayOutput
}

type WorkspaceTagArray []WorkspaceTagInput

func (WorkspaceTagArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]WorkspaceTag)(nil)).Elem()
}

func (i WorkspaceTagArray) ToWorkspaceTagArrayOutput() WorkspaceTagArrayOutput {
	return i.ToWorkspaceTagArrayOutputWithContext(context.Background())
}

func (i WorkspaceTagArray) ToWorkspaceTagArrayOutputWithContext(ctx context.Context) WorkspaceTagArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceTagArrayOutput)
}

type WorkspaceTagOutput struct{ *pulumi.OutputState }

func (WorkspaceTagOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*WorkspaceTag)(nil)).Elem()
}

func (o WorkspaceTagOutput) ToWorkspaceTagOutput() WorkspaceTagOutput {
	return o
}

func (o WorkspaceTagOutput) ToWorkspaceTagOutputWithContext(ctx context.Context) WorkspaceTagOutput {
	return o
}

func (o WorkspaceTagOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v WorkspaceTag) string { return v.Key }).(pulumi.StringOutput)
}

func (o WorkspaceTagOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v WorkspaceTag) string { return v.Value }).(pulumi.StringOutput)
}

type WorkspaceTagArrayOutput struct{ *pulumi.OutputState }

func (WorkspaceTagArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]WorkspaceTag)(nil)).Elem()
}

func (o WorkspaceTagArrayOutput) ToWorkspaceTagArrayOutput() WorkspaceTagArrayOutput {
	return o
}

func (o WorkspaceTagArrayOutput) ToWorkspaceTagArrayOutputWithContext(ctx context.Context) WorkspaceTagArrayOutput {
	return o
}

func (o WorkspaceTagArrayOutput) Index(i pulumi.IntInput) WorkspaceTagOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) WorkspaceTag {
		return vs[0].([]WorkspaceTag)[vs[1].(int)]
	}).(WorkspaceTagOutput)
}

func init() {
	pulumi.RegisterOutputType(ConnectionAliasAssociationOutput{})
	pulumi.RegisterOutputType(ConnectionAliasAssociationArrayOutput{})
	pulumi.RegisterOutputType(ConnectionAliasTagOutput{})
	pulumi.RegisterOutputType(ConnectionAliasTagArrayOutput{})
	pulumi.RegisterOutputType(WorkspacePropertiesOutput{})
	pulumi.RegisterOutputType(WorkspacePropertiesPtrOutput{})
	pulumi.RegisterOutputType(WorkspaceTagOutput{})
	pulumi.RegisterOutputType(WorkspaceTagArrayOutput{})
}
